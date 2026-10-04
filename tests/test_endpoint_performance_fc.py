"""Offline FC service contracts: fresh Sessions, real SQL, full JSON parity.

These exercise the endpoint-owned service functions, not the application/router.
SQLite statement counts are not PostgreSQL execution-plan or latency evidence.
"""

import base64
import json
import zlib

import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import backend.fc_activity_insights as fc
from backend.database import (
    FCActivityCase, FCActivityClassification, FCActivityMotion, FCActivitySummary,
)
from performance_helpers import count_statements


# Complete JSON responses captured from the unmodified service on this fixture
# before optimization. Compressed only to keep the duplicated labels/notes small;
# comparisons below decode these to ordinary JSON, never compare digests/subsets.
_BASELINE_JSON = {
    5: (
        "c-rk;TW{Mq7XB-OUYcUvtmxJaHuKc&w7XNZlR>AzJQRUJTeQPQ7cV6xHH!TAJ%^+uN}?1gmXZt_AV^}7;<@nf@Lay+>koIsgOrKHJ^gVrbJIAb!4e)Zc(9nc7mWG=j~I-)0i#!J>9aLYcpSm_%b9+*6*Nkhf~GLfJAVE8^~ucrmic_mVKKq3IJ-9An>R<RD*$1^k~p|x{&KZnuHh{frS2&K4*d*fsdaw1KHVq9%F8rH&Uv(z+|m^b+*9|9;Hxa6fs;>j(%8|{X6`!9aAA-nWIm@6P@lQG`9l3XfuF=fqDV)*gj9A+Y}gvPFe$y4<G4KC?E=0AiJm2nVCz`;{Ya4}sjAZL<m8+}zJ8?UIVp1ofgWtQsA=${Twcy#KGMtQ^dj^!C#2s(BCz}0Q0{0+<-cke*Dr>95qQ;9+J?i1FMXcu;)J(vlbq(nS-Orx){ofY2B@tBqnCbst!z+QYSyGuU0cN0F#GEd_lgD?7`dB8mk}&cl7-DLM;oVyCm~M~=J%YhcdKQ#+H=7+S^J8%18B@VN3G`vZx#D{Q}|!=qn1TJ6OQ7^rUWilOR+Opn42s#R8$$g;t5^Gn+;#HI%9@>QYAF0Zq8p9dwpoGDW1?=4-NjJI9=+)yb4ScF&T-|3np5$hzn?MQPniE2`b*jpdmPUHbebf41*iVCphpWS?^_23r%MSq+lIdC-EkCR8DP<WpP|Gfw%6mSMc7ZE`5^H{Sv;VSz@yECp>oI4KNhO@VXPm%G>uBH+M8)>@#!a5BiK~d(7RKvx!AW(*Xp)A{f|JllS)w%pC~4jWdy=5O3tn0ZXr$Nco1tvHM@flKOVN%}1SLwExmO5w98eHPB2zqisgF743Y~&yZ~}XuKk=Huf&s20XdAlNr1hELvaG4M88UR9@lxU4^SJ@EJKW=Gd63xxc#T%1bPRc-=SwXL1N6rm4I^eY+!Q$W`$GXEiT0msHvJltt1%#+zlz!-`<<@<FL@7`%g_e~Wok_@^kXnBoT<D+7_lIoi+=Za$Vgw^7)$q-D>dxbIf$O94+)^=d!cu}Ioe;#~9e!igY4g6Qdrr+Ykn&io(F9?oJiEo0y{{iXe~K2z6pZu&S=^6MOJMV#$kfIx6E)HA#OT6QQ8Nnn35icXSRAOdTmMtCIY{`UEgH%@ZwoXnkohddo_h<Ji{$l9)b46hq^5Qe8M9KLD9u{pahJqKeh=jd|=Y9ikA``|T%D*@sfKMPy<t=yR9>=vfU^E+HB*F1vA&lb4C>JU@@OVgkmNUC&@q3JEG^b~LTx)rJzYVMbKG~^rVm$^q?NyEYnjZ`u)a9!n-JgULi^_!?nfRAN7iQ~;IjvO1WmCta83N{u68}kMmUV{x%Wy9;mhG$_T%7UQ6$LmAX(cpvhRR{2Pb1rwN76-#t)t(qeH9%wDT{MQ;X;oRBtup*>Wotgzo(3pzVPmQq*SGHM)D{L?3&A^{(9iHNae#(-hf%n=R|yl4Ar+bTvGW(@sl3g>0SM-R&p~JKi}504gw6^w1{g^7tblD&%oLAZR7VKTz^IjwS+ziexiM27<dUJfXt2AWps0vqfZ@K;9~;G*xn25&(o%(B^W5hd@v=RW$2l^BsV$}-HWrlOe|4&SWbrsk&=pG!IsdIbHN@<+zD_Z{USg{A)mKu_CaGtUv}SUu<RYYr$O}Q=Bya<RB{-l1S;ByrLE6JF&WF#H*&!1gV!oVhut3Een62+1@ycwGVU&_U&=Fm#3J;YQ>+83Uoj(MaYz)kSM&Pw0nj|sA+o`6XJa=SHB%F})C{R(Ij%SaZKSLS>ij*>VSO>z1fMZTw8hv@vD+ZsZou$Rc5i9NB?ASSrn8kyQXZqGsq+yupbzJiEMSkdD=0F2&sf(7T^H%B0;nGZC55Wo16}lY?StAt~mOz}VJkpWQH`me{;4ykM%!klU^88qBEsfT&&od{9(eA(*;!f^hJ<O=p=BmB4)RXhn1}n;#;VJ*6ay@kxAVbm#KOSm(DZtH-n9{6y1693zL$m03eL>*@#>rTd0h8C0i%+^vq!~9I0XP74L{uRVgtIxcZG6Q<gvZT#_iAa^S(3(~A!PBuDx23OoAO15a9%|?Viyhsh<qswX_r$iZ4p%s^pmxj0MFX<UsD65RRg4|0k5{Z-eJ3Y^3oeFw2lMy@%xXE)wCjH&@$<uLAzSR)52K_!M{qH|12rs@kRHZa9<ZER*;EqFH-qbJM$y_{S%LPf`?kaQKbCN^#xOTWidrLb)Di~F|(@j{MdQ+do1q)=0Af2eT5fI&OLrg=_RbU+ROLBgv>(GOr23okwqLT3P5rO7ZzMM9NfP)I*W_A+;M4^Wz%V3qe;|zOQPxM6PBj=p{Q-Xs-~WLMJ_D0<et8=2PFEbzBAP!+GJ6ruP7MYvOKvr)45qW_Oa;K_~x9K%{h%S{@k4NL0|7!6P9KnZ~gYkmFlOZLvVgy`KE4*$ZfC8y%~^;wr=FKNvg?v^X<~kZiZwVZL%z;O>}GfU=H34NQ2wB&x2ZPirj1gJzx&nEdD%bo^Ee(J!C4p+UI<jdv{i2ZGPY7D8<>Dr&XK!5{o!W<HuoBXK6~Wsr#_SvQ`5p_iy0m!$BOsc3?N=WxIYcF?OSi)X3NkgVgIuu^U~4M!{|v1WqQ$Zgdfo*o`8`m@)zF$~U{B7#+Nflqz;5hMfV(JtcBod0SV6A@el!BCz#vR<SUl^M`t`ZK__BwQV*Xv6jBqElsOt&#GV7357F(Gebmcg}ZdYWzL%jmFZw7KU^M$%P0$1z{IKh+ow-2$P2Q-Su|lwUB!F%oq}mG=gN6YBkJSrZDvClaO7#C5o|;>%>=&wTNv`K$k7VxfF=pTHpCK>YAGOC>vuW195%2Cje7%>lLa6`ahk9&dO?GLMO)@qrZ&+O7IZ{$+lG+Ti`)eiPknjrTuh%{cm%%8SCVY?4fZ#GNgq4ka3!gRTuK#bT^CNp%}uyGvnHvz+s{eM_NZA&a8(rOI(k1Gy=P0TNaU%Yd;oi;v#GXzSRDvUZUMq}gof=XSaKT*wxjes4GPvPFHc?n!~0YJda@{XaKwn}jwBC>tOk)BBf=U)@Q_IBj><eN;_63qEYxf-T<k>H)O*5~-WN8MOo<Jh4B|<qhIo?cAf9A8h$k5n;@Pf~$#9xvDx4;n8j4BAhGO0iuJTcUB*}e&B&WwZJ|4Uxc@VrJ>A)-g4FGzLF2qA{`snaxha^x9pxP6D>*vF7<w<#2BRRmLnn<vA<Q2Im<dye0kyp9ii{4YW+M7VFxdo{8^T2rq)!@nB8?N;PUAiN5={Dc?s(Q#?%{qdPUPaq_s%~W6WwvMheO}(MFWdBHVBhg4!}3lrpyh?*mC)NJWNTb!t1wnMj>hYa*CJ!$wMY-V7U_Z4B17<6<R`^z4TcDjhryZjK){g4ihy|t#>PZ>koJGdFfzzv7^Oox5q&6)(SYbf=a9a`FpVA7Zs?>nBEEz4#CLc@@f`zk3l^}zt?&c;J9j`4kh`G>$Z!<FU=)CE<~PGJ+$OaCdJosTrH9)EVry^WdfiQ2_5M>A_o<8f)W!XJNLzM<&g+O>)k7PnhxA6rXn!8o;XJH~d2pZdpjPA|UB)pQiKFxiM{5U8)bSg$sW(mEZsP9T1P!=acg>zMKb9Vn=Xq`aw&1BpVpmYv+<4Rtg+_E;Burk}F?cE|A6Qa0v|KB-db44fi>N0nw!b~Rz1W)PF=oBBtqoc)xO%+`u3nFVtJkC8>J2HldV>nCUbW!b>VnNmVWm7ba!Kqd(R)htrc3n7LRzniRZCH-qwZuYE!pcvw$jk~&H4WUl!#L+"
    ),
    50: (
        "c-rk;TW{OA68<ZMUYg>#S<|f>oa|G#+n&>+-7LBV_Mr$2+M*pcy7*91QX|NJKf{|uNt7blQj$dj1cfb;oZ)b0IG4};cH^yCkW!v_r#H6~FO5?YEZ`A^2lMH~yP(7mSVZBq7f^CV7d~CFgvAjIcnJg4!wn}<y5J;*fz#vHuV0@`yziOMRt%Qo^or4Id*W<be_dW;KJhqB;^2z<i{);yf@w5Ly;D2|F8vIKsg-U#pX`!+?L`_3?pd^v43i}dyi@NhXUi-i0W!l-8Y4Yy;;rILtSmMYQlF6s=uf=uZ0?=D!0_Q@ZpaEsYMP+4rF>0Sf)AV4d-+}vAlq%gR<NmO3F34WbH6JwTqjnRy_=vMlkc%Bv6&%epCnL(ljjvVev$;_2<i)pW=uy?FAXU@PmlpM*o5+E3p)Q*uLXttbw?7f>Y`gSIQoUpl5L!@=HrsXP@JW!IHX<4&2NF;l2dZ&$Ja_9rP^k7I_1@Qd<~<&-FR0d$Ux)0EV_(fiGr|Dx#D%rm{=0BB%yxS3HsEUhO5Kpbe*-V>9R<B=(!NSvBYKU?`#SDZfq}$e9Dnx%OwfMmkYkNn3$EAs0ph4`idoF5wF*5MQglSo0NhfN%@fezSwCax+cPAjWB8~Msd2(=DiF`%3`w;rx%nr$x<w#JxE31f>V(6HU>F?DY~@wOa2;siy466PjcT$z2=6{7HGjjq)OwBabKu1#<99sGl5zA9U07A*CddnWVe8S(k!vL`U@VTcnv&-G0aC{tS*8cTQ<%ojD2b^{ZU(tR!!sF&^qQJN&8R$)u5nYb?)C&P<^2AHqLk|w(&-e?6dZY@|3L^7~%ginp6+%t$B;`w>{S0@_0qT*MV>X5^XZFDGBJ4ekK?P)fP9XQ`g=_n}8)3duqdbPNUUDO&_$mrSg*BZA*-Oh3|qXYmAGpic73*UwMs15U*;+a3){Du1P8{Sl{gzYFjHigtLlUnkl;UM@l2<GvoClWnpP=@61anb$Gdt%72eplzXfwE$QS(@vaC~5_GgCA>4{IdF~>yqe;`rMRDgNH<yJlt@7P}wxyBOtOQ-N^a4c?NI{Tw#nPRyL^S&s+JRvvqw@x?)L*zS^D}jg8#@pqCClh&!{coG0`>%EqMo^>*mO`PYJqbWQFoG5Vij0aNQFg`@P{vdzCp<`I+>w>g)H4eC51JykT!+|A{?(@P9m6XVDe2Z>NOm{oFWmKp`$Muhzd`i-xIqbTon-f_*vM%a_KfLMmO+{pYL<oT(bxwL|2dt%R}_}Z%u@(AsN#_h$c995>(8Yb<1Q$OuAbLGm%r&huIXrk_skLJ6z7(z?)f*OyDEp-S50S0=^fa=czOQ!^hUV;+Z(7oRfLZ$*j&voe^B&q#Gks2P07y1SL*hA10F;C%CgrfW6yuc~X^_8IG*-#8R(5V%tk<LPCvVtMXOE>dk!3_E4-oQk=UOE2ja?Cp@~Y!3jgCFD&*8JWLP}v9C7*_xduS9I~oBb3aCZ6PC)$9vlLv2%L~`4!>FxA(KQ)NHE|<sz(KMor(<e*b@Q?!8uqJ7d$B!dPH7Ll}EXxLSQ7=UJwvfL`3}Iz0qH5HJ@3-_UB4W7DcBQFv;|yxeg%4$PlNxntobaQKkx&vGSS21F6j}X=?5DH}$Qy)pjLp-|Do}R+X)F-tE-2Ti0eQny2bETxyEEC-emamoq2?0x`%M2t*W8Eq+BGzm!IYlrsnn4d0-MiaF3;9|_{6(L56|OadWEbg9ZjL@KVYXC0$IIcRPS%z;Q?+7U^T7y|QD(@&lwnL%+B5*7t2?$c54G5RYcL7+$}y@z!m(g>JH#S7gxCSTEelc^SpA4jxMg|lOH7EzZw8`1=vl}$@M)9bik>8t$G#?Qfe+Ei&RH0Z4o8)8yh;3&Z*k)?1#1Tsy+MbHA#u<}nwI!9eerGUr6zlroosEf&})d`bm1;;%>Ni5V4T%$P9EvzT<aCOG&NF7yblLyH<wMYq-J5$M_vI)qibfG}lx4VSk8B^2ZE!|3Gw_g*l@WehRa52l#qNW4duSe(Kbfrl%Z#xBW2FhAgZ4ox;@^72?it<QUp7T!D8(w8e8i&?C^9SzjweC(iCTn};-QkAq!4@K4Zbuf(8@8$zckEWZ=(gQ@(mZL-nQbB9W+C8;6sDCkKJbW7UQYXOTStl74*$btK`xIZ^saO)p<S=#dBLbc@VAoYF9ii*$HLtw%-2PYB_yt!i&Q?<&izPy{>&nl2<z4}@;U*!zMv`#&4(x_uQTE+YL{c4AERe~#PV*S{xh)bD{=7{?!~v1T*7+GotzI^WEYtx%2q{2&Err}0Fo29z~K5}a2;s9bNGtOEt8sQ^|bo-v3RX@#p|9wp=p}iMnwTsRrYk6r_NGR-s!7`Kt(^*7pXR;brwbX;)1suY6=3S+;396{FHZteCk*8>GGgjZ(vp$^ikjYqQETmLxuw_qf2E}SL5OQ9urjEbCF6=9(>y)du=?^vC~?ceaCc5?QZ+zB~AO8kDeS?&ZG49wny&Vv;!0SI`is!kLiK))_VQuVH13J8|`89=jG0DVjtmIg}K=Sl(ZCcE0&hE>ub#8D2*SFcAcduxhCF27u_0_9Y27wpZCX+{N4f|nOQi2xyA`hM?#OZ(i#{%V$*tEr8Ovaq?OVj&=H%$NtMFj$dOiR5;&6QB;%&7tyyYYoTI~=p%Tp2bh0%-xwq`EE!k^}KV)(zTneZF*sUmQ=%l0C&Kt4U<?PIjO0S`{c2{4l-WKcF*b+Om!8^V7*NnJn#q6BdK{BHvUv4}WhKnc*m%zxW_u=#B7x)F9i(w?83tbg__k)0<QFMjgl8E@?Znv{25t5iJ(+Wo-l4e{?{}6_3!wphm6_6wmuo1oxdAZyp=<W|WxOi>BB5D^3$R`V654mxPTI&S~0vc_oUm99RayXC~`9&O(OCbm467r|Mv_em$TrZ{={_H79w)_r<Y$j<V^exwtYCxzIk(PDtWIUtFg$3KBW?nbXE&H%`F~U=EqKEW(Abn;FQPeQ$qkI5orL(W5ep?l)i|>N!wuO$(I9+@vPPe6+Jq}FQx>R)?QQWKg<H<Zf!~w&tJxLxCb@d`SMDW#%;2|;Cp29pV6zfKGC@60?tnNr)+53XJ-WyOAj|x;B4{eG^N1Ngi(WZDrv?(4GZQ3H1(Ey`(G{7hx9TJKMhlJh}y7O@WHSxUxHSYm!`H1k6_+jvpxD7A)&%g%OdKnMI?4yIZ9g<zu@NrL&v7Zt$W|H=zhH`*X)xl@YNH2VUNUui<^fIE)n^*0Uuj9gIE?n5pgd6HryT|`{aM%+}YEPKdT~6**+0<T5T4In+)!k|`Z{_7hDro(V(6s-HroSEUxBS*wUJe$zJ@>#8_FIRC4eoUnn#+K6x<kY8u+T8v1saCCK*Mk^Xc+#fp<%sINch1pEFAzg_z?qa9*DOg0VLS*A59pzz`*#Co}><GWOO1mL<6G}p+g!MJ%x5y!=jzofY1@#89LG%Inomi;esFB32A7Uv<EH$?}<ymd*BlKqY4Z(pdPb{!xDy2?Fir15N<=uH8+Is=m)F$PYvOxhVWBE_}d{3-T_*;19oQ*?Y|z<VI87}dRUkAus-O)oz8=LnTK>Khv-8N(rFy5mpD?laL9h(I32%{+j=83?kY_=cP9N<noiT{wCTTBc<QLQ1yr;`9(C`b7G39wlhs>zsyiQ8cebQlsmHp?vF*R}sU$0|Uq0Sljx~9VU6E~SnpP{a-3qc@>aktQvAwFX{fe=bT5O{WwyTGwdfmVUvZqAvDbX7*(JKmSo$6K%m8q86ldHPqt{k~)L+7{W{|ABGfFA"
    ),
}


@pytest.fixture(params=[5, 50], ids=["5-files", "50-files"])
def corpus(request):
    engine = create_engine("sqlite:///:memory:")
    for model in (FCActivityCase, FCActivityClassification, FCActivitySummary, FCActivityMotion):
        model.__table__.create(engine)
    factory = sessionmaker(bind=engine)
    fc._CACHE.clear()
    with factory() as db:
        for index in range(request.param):
            kind = index % 5
            case_id = index + 1
            year = [2014, 2015, 2016, 2015, None][kind]
            city = ["Toronto", "Ottawa", "Toronto", "Ottawa", None][kind]
            imm = f"IMM-{case_id}-15"
            db.add(FCActivityCase(id=case_id, source_key=imm, citation=imm,
                                  raw_payload={"unused": "x" * 10000}))
            db.add(FCActivityClassification(
                source_case_id=case_id, source_key=imm, imm_number=imm, year=year,
                city_filed=city, case_name="Example v Canada", nature="Immigration",
                classifier_version="fixture",
                classification_json={
                    "leave_decision": {"result": "granted"},
                    "challenged_decision": {"application_type": "judicial_review",
                                           "decision_date": "2015-01-01", "unused": "x" * 10000},
                    "timeline": {"filing": "2015-01-02"},
                    "motions": [{"type": "stay_of_removal"}],
                    "procedural_events": ["x" * 10000],
                },
                source_name="unused " + "x" * 10000,
            ))
            summary = FCActivitySummary(
                source_case_id=case_id, imm_number=imm, classifier_version="fixture",
                year=year, city_filed=city,
                leave_result=["granted", "refused", "granted", None, "unknown"][kind],
                review_result=["granted", None, "dismissed", None, "unknown"][kind],
                resolution=["judicial_review_granted", "leave_refused",
                            "judicial_review_dismissed", "resolved_by_consent", None][kind],
                decision_body=["irb_rpd", "visa_office", "irb_rpd", "", None][kind],
                leave_judge_key=["alpha", "alpha", "beta", None, None][kind],
                leave_judge_name=["Alpha", "A. Alpha", "Beta", None, None][kind],
                merits_judge_key=["alpha", None, "beta", None, "alpha"][kind],
                merits_judge_name=["Alpha", None, "Beta", None, "A. Alpha"][kind],
                applicant_counsel_key=["one", "one", "two", "two", None][kind],
                applicant_counsel_name=["One", "O. One", "Two", None, None][kind],
                representation=["counsel", "self", "counsel", None, "unknown"][kind],
                proceeding_language=["English", "French", None, "English", None][kind],
                application_type="judicial_review", office_location=["Office", None, "", "Office", None][kind],
                leave_refusal_reason=["", "not_perfected", None, "other", None][kind],
                joint_applicants=[True, False, None, False, True][kind],
                dormant=[False, True, None, False, True][kind],
                filing_timeliness=["on_time", "late", None, "", "unknown"][kind],
                record_timeliness=["on_time", None, "late", "unknown", ""][kind],
                memorandum_timeliness="unknown", hearing_window="within_window",
            )
            # Nulls, negative values and inclusive/exclusive bounds are deliberate:
            # insights and dashboard historically differ on negative durations.
            for offset, field in enumerate(fc.DURATION_FIELDS):
                setattr(summary, field, [0, 10 + offset, None, -1, 3651][kind])
            db.add(summary)
            db.add(FCActivityMotion(
                source_case_id=case_id, imm_number=imm, position=1, year=year,
                city_filed=city, motion_type=["stay_of_removal", "extension_of_time",
                                            "stay_of_removal", "custom", "custom"][kind],
                filer=["person", "government", None, "person", "government"][kind],
                outcome=["granted_in_part", "dismissed", "withdrawn", "pending", "moot"][kind],
                judge_key=["alpha", "beta", None, None, "alpha"][kind],
                judge_name=["Alpha", "Beta", None, None, "A. Alpha"][kind],
                days_to_decision=[0, 730, 731, -1, None][kind],
                relief="x" * 10000,
            ))
        db.commit()
    yield request.param, engine, factory
    fc._CACHE.clear()
    engine.dispose()


def calls():
    """Nonempty, filtered, empty, thresholds, every dashboard filter, case lookup."""
    common = dict(year_from=2015, year_to=2016, decision_body="irb_rpd")
    return [
        ("insights", {}),
        ("judges", {"min_decisions": 1}),
        ("counsel", {"min_files": 1}),
        ("motions", {}),
        ("dashboard", {}),
        ("case", {"imm": " imm-1-15 "}),
        ("insights", dict(common, city=" Toronto ")),
        ("judges", dict(common, min_decisions=1)),
        ("counsel", dict(common, min_files=1, city="Toronto")),
        ("motions", dict(city="Ottawa", year_from=2015, year_to=2016)),
        ("dashboard", dict(city="Toronto", year_from=2014, year_to=2014,
                           decision_body="irb_rpd", application_type="judicial_review",
                           representation="counsel", language="English", office="Office",
                           resolution="judicial_review_granted", judge="alpha", counsel="one")),
        ("insights", {"city": "missing"}),
        ("judges", {"min_decisions": 1000}),
        ("counsel", {"min_files": 1000}),
        ("motions", {"city": "missing"}),
        ("dashboard", {"city": "missing"}),
    ]


def test_full_json_and_statement_ceiling(corpus):
    size, engine, factory = corpus
    expected = json.loads(zlib.decompress(base64.b85decode(_BASELINE_JSON[size])))
    ceilings = dict(insights=24, judges=3, counsel=1, motions=1, dashboard=2, case=1)
    counts = []
    for (endpoint, kwargs), baseline in zip(calls(), expected, strict=True):
        fc._CACHE.clear()
        fetch = getattr(fc, f"fetch_fc_activity_{endpoint}")
        with factory() as db, count_statements(engine) as counter:
            cold = fetch(db, **kwargs)
        counts.append((endpoint, counter.count))
        assert counter.count <= ceilings[endpoint]
        assert cold == baseline
        if endpoint != "case":
            assert all("classification_json" not in sql and "raw_payload" not in sql
                       and "relief" not in sql for sql in counter.statements)
        if endpoint == "case":
            assert "source_name" not in counter.statements[0]
            assert "classified_at" not in counter.statements[0]
        if endpoint == "dashboard":
            assert "source_case_id" not in counter.statements[0]
            assert "stay_status" not in counter.statements[0]
        if endpoint == "insights":
            duration_queries = [sql for sql in counter.statements
                                if "days_decision_to_filing" in sql]
            assert len(duration_queries) == 1
            assert all(field in duration_queries[0] for field in fc.DURATION_FIELDS)
        with factory() as db, count_statements(engine) as warm_counter:
            warm = fetch(db, **kwargs)
        assert warm == cold
        assert warm_counter.count == (1 if endpoint == "case" else 0)
    print(f"MEASURED {size}: {counts}")


def test_cache_keys_do_not_cross_filter_slices(corpus):
    size, engine, factory = corpus
    expected = json.loads(zlib.decompress(base64.b85decode(_BASELINE_JSON[size])))
    # Keep all distinct endpoint/filter/threshold keys resident together, then
    # revisit in reverse order using new Sessions: no identity-map assistance.
    for (endpoint, kwargs), baseline in zip(calls(), expected, strict=True):
        with factory() as db:
            assert getattr(fc, f"fetch_fc_activity_{endpoint}")(db, **kwargs) == baseline
    for (endpoint, kwargs), baseline in reversed(list(zip(calls(), expected, strict=True))):
        with factory() as db, count_statements(engine) as counter:
            assert getattr(fc, f"fetch_fc_activity_{endpoint}")(db, **kwargs) == baseline
        assert counter.count == (1 if endpoint == "case" else 0)


def test_cache_ttl_is_not_refreshed_by_hits(corpus, monkeypatch):
    _, engine, factory = corpus
    clock = [100.0]
    monkeypatch.setattr(fc.time, "monotonic", lambda: clock[0])
    assert fc._CACHE_SECONDS == 1800
    with factory() as db:
        cold = fc.fetch_fc_activity_dashboard(db)
    clock[0] += 1799
    with factory() as db, count_statements(engine) as counter:
        assert fc.fetch_fc_activity_dashboard(db) == cold
    assert counter.count == 0
    clock[0] += 1
    with factory() as db, count_statements(engine) as counter:
        assert fc.fetch_fc_activity_dashboard(db) == cold
    assert counter.count == 2


def test_cache_lru_eviction_and_expired_entry_pruning(corpus, monkeypatch):
    _, engine, factory = corpus
    monkeypatch.setattr(fc, "_CACHE_MAX_ENTRIES", 2)
    clock = [100.0]
    monkeypatch.setattr(fc.time, "monotonic", lambda: clock[0])
    with factory() as db:
        toronto = fc.fetch_fc_activity_dashboard(db, city="Toronto")
        ottawa = fc.fetch_fc_activity_dashboard(db, city="Ottawa")
    with factory() as db, count_statements(engine) as counter:
        assert fc.fetch_fc_activity_dashboard(db, city="Toronto") == toronto
    assert counter.count == 0
    with factory() as db:
        fc.fetch_fc_activity_dashboard(db, city="missing")
    assert len(fc._CACHE) == 2
    with factory() as db, count_statements(engine) as counter:
        assert fc.fetch_fc_activity_dashboard(db, city="Ottawa") == ottawa
    assert counter.count == 2  # Least-recently-used Ottawa was evicted.
    assert len(fc._CACHE) == 2
    clock[0] += 1800
    with factory() as db:
        fc.fetch_fc_activity_counsel(db)
    assert list(fc._CACHE) == [("counsel", 20, None, None, "", "")]


def test_cache_default_capacity_and_failed_builds(monkeypatch):
    fc._CACHE.clear()
    assert fc._CACHE_MAX_ENTRIES == 256
    monkeypatch.setattr(fc.time, "monotonic", lambda: 100.0)
    try:
        for index in range(257):
            fc._cached(("bounded", index), lambda: {"value": index})
        assert len(fc._CACHE) == 256
        assert ("bounded", 0) not in fc._CACHE

        def fail():
            raise RuntimeError("fixture build failure")

        with pytest.raises(RuntimeError, match="fixture build failure"):
            fc._cached(("failed",), fail)
        assert ("failed",) not in fc._CACHE
        assert len(fc._CACHE) == 256
    finally:
        fc._CACHE.clear()


def test_case_errors_are_bounded(corpus):
    _, engine, factory = corpus
    for imm, status, ceiling in (("bad", 422, 0), ("IMM-999-15", 404, 1)):
        with factory() as db, count_statements(engine) as counter:
            with pytest.raises(HTTPException) as error:
                fc.fetch_fc_activity_case(db, imm)
        assert error.value.status_code == status
        assert counter.count == ceiling
