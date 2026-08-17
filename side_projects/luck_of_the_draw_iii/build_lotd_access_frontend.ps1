param(
    [string]$CasesCsv = "side_projects\luck_of_the_draw_iii\output\access_staging\lotd_access_cases.csv",
    [string]$SummaryCsv = "side_projects\luck_of_the_draw_iii\output\access_staging\lotd_access_docket_summary.csv",
    [string]$OutputPath = "side_projects\luck_of_the_draw_iii\output\luck_of_the_draw_iii_frontend.accdb"
)

$ErrorActionPreference = "Stop"

$acImportDelim = 0
$acForm = 2
$acDetail = 0
$acLabel = 100
$acCommandButton = 104
$acTextBox = 109

function Add-Button {
    param(
        $AccessApp,
        $Form,
        [string]$Name,
        [string]$Caption,
        [int]$Left,
        [int]$Top,
        [int]$Width,
        [int]$Height,
        [string]$ControlTipText
    )

    $button = $AccessApp.CreateControl($Form.Name, $acCommandButton, $acDetail, "", "", $Left, $Top, $Width, $Height)
    $button.Name = $Name
    $button.Caption = $Caption
    $button.OnClick = "[Event Procedure]"
    $button.ControlTipText = $ControlTipText
    $button.FontSize = 10
    $button.FontBold = $true
    return $button
}

function Add-Label {
    param(
        $AccessApp,
        $Form,
        [string]$Caption,
        [int]$Left,
        [int]$Top,
        [int]$Width,
        [int]$Height,
        [int]$FontSize = 10,
        [bool]$Bold = $false,
        [string]$Name = ""
    )

    $label = $AccessApp.CreateControl($Form.Name, $acLabel, $acDetail, "", "", $Left, $Top, $Width, $Height)
    if ($Name) {
        $label.Name = $Name
    }
    $label.Caption = $Caption
    $label.FontSize = $FontSize
    $label.FontBold = $Bold
    return $label
}

function Add-Textbox {
    param(
        $AccessApp,
        $Form,
        [string]$Name,
        [int]$Left,
        [int]$Top,
        [int]$Width,
        [int]$Height,
        [string]$ControlSource = "",
        [string]$ControlTipText = ""
    )

    $textbox = $AccessApp.CreateControl($Form.Name, $acTextBox, $acDetail, "", $ControlSource, $Left, $Top, $Width, $Height)
    $textbox.Name = $Name
    if ($ControlTipText) {
        $textbox.ControlTipText = $ControlTipText
    }
    $textbox.FontSize = 10
    return $textbox
}

function Add-BoundField {
    param(
        $AccessApp,
        $Form,
        [string]$FieldName,
        [string]$LabelText,
        [int]$Left,
        [int]$Top,
        [int]$LabelWidth,
        [int]$TextWidth,
        [int]$Height = 300
    )

    Add-Label -AccessApp $AccessApp -Form $Form -Caption $LabelText -Left $Left -Top $Top -Width $LabelWidth -Height $Height -FontSize 9 -Bold $true | Out-Null
    $textbox = Add-Textbox -AccessApp $AccessApp -Form $Form -Name ("txt" + $FieldName) -Left ($Left + $LabelWidth + 120) -Top $Top -Width $TextWidth -Height $Height -ControlSource $FieldName
    return $textbox
}

function Add-VbaModule {
    param($AccessApp)

    $code = @"
Option Compare Database
Option Explicit

Public Function OpenCasesByIMM() As Boolean
    DoCmd.OpenQuery "qryCases_ByIMM"
    OpenCasesByIMM = True
End Function

Public Function OpenSummaryByIMM() As Boolean
    DoCmd.OpenQuery "qryDocketSummary_ByIMM"
    OpenSummaryByIMM = True
End Function

Public Function OpenCasesMostDockets() As Boolean
    DoCmd.OpenQuery "qryCases_MostDockets"
    OpenCasesMostDockets = True
End Function

Public Function OpenSummaryMostDockets() As Boolean
    DoCmd.OpenQuery "qryDocketSummary_MostDockets"
    OpenSummaryMostDockets = True
End Function

Public Function FindCaseByIMM() As Boolean
    DoCmd.OpenQuery "qryFindCaseByIMM"
    FindCaseByIMM = True
End Function

Public Function FindSummaryByIMM() As Boolean
    DoCmd.OpenQuery "qryFindSummaryByIMM"
    FindSummaryByIMM = True
End Function

Public Function OpenWorkbench() As Boolean
    DoCmd.OpenQuery "qryWorkbench"
    OpenWorkbench = True
End Function
"@

    $component = $AccessApp.VBE.ActiveVBProject.VBComponents.Add(1)
    $component.Name = "modLotDFrontend"
    $component.CodeModule.AddFromString($code)
}

function Build-HomeForm {
    param($AccessApp)

    $form = $AccessApp.CreateForm()
    $form.RecordSelectors = $false
    $form.NavigationButtons = $false
    $form.DividingLines = $false
    $form.ScrollBars = 0
    $form.Caption = "Luck of the Draw III Workbench"
    $form.Width = 17000
    $form.Section($acDetail).Height = 9000
    $form.AllowAdditions = $false
    $form.AllowDeletions = $false
    $form.AllowEdits = $false

    Add-Label -AccessApp $AccessApp -Form $form -Caption "Luck of the Draw III Workbench" -Left 500 -Top 400 -Width 9000 -Height 450 -FontSize 16 -Bold $true -Name "lblTitle" | Out-Null
    Add-Label -AccessApp $AccessApp -Form $form -Caption "Use the buttons below to open IMM-sorted datasets, prefix lookups, and high-volume docket summaries." -Left 500 -Top 1000 -Width 15000 -Height 400 -FontSize 10 -Name "lblIntro" | Out-Null
    Add-Label -AccessApp $AccessApp -Form $form -Caption "The full 2.6M docket rows remain in PostgreSQL; this Access front-end imports the case and summary slices only." -Left 500 -Top 1400 -Width 15000 -Height 400 -FontSize 10 -Name "lblScope" | Out-Null

    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdCasesByImm" -Caption "Browse Cases by IMM" -Left 700 -Top 2300 -Width 3200 -Height 550 -ControlTipText "Open the full Cases table sorted by IMM number." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdSummaryByImm" -Caption "Browse Summary by IMM" -Left 4300 -Top 2300 -Width 3200 -Height 550 -ControlTipText "Open the DocketSummary table sorted by IMM number." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdWorkbench" -Caption "Open Workbench View" -Left 7900 -Top 2300 -Width 3200 -Height 550 -ControlTipText "Open the combined case and summary workbench query." | Out-Null

    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdFindCase" -Caption "Find Case by IMM" -Left 700 -Top 3200 -Width 3200 -Height 550 -ControlTipText "Prompt for an IMM number or prefix and search the Cases table." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdFindSummary" -Caption "Find Summary by IMM" -Left 4300 -Top 3200 -Width 3200 -Height 550 -ControlTipText "Prompt for an IMM number or prefix and search the summary table." | Out-Null

    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdCasesMostDockets" -Caption "Cases with Most Dockets" -Left 700 -Top 4100 -Width 3200 -Height 550 -ControlTipText "Open cases ranked by document count." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdSummaryMostDockets" -Caption "Summary with Most Dockets" -Left 4300 -Top 4100 -Width 3200 -Height 550 -ControlTipText "Open the summary ranked by document count." | Out-Null

    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdYearFilter" -Caption "Filter by Year" -Left 7900 -Top 3200 -Width 3200 -Height 550 -ControlTipText "Open the year filter form." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdCityFilter" -Caption "Filter by City" -Left 7900 -Top 4100 -Width 3200 -Height 550 -ControlTipText "Open the city filter form." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdCaseDetail" -Caption "Single Case Detail" -Left 11500 -Top 2300 -Width 3200 -Height 550 -ControlTipText "Open the case detail lookup form." | Out-Null

    Add-Label -AccessApp $AccessApp -Form $form -Caption "Tip: all datasheet windows retain Access column filters and sorts, so IMM-number browsing stays simple after opening a query." -Left 700 -Top 5200 -Width 14500 -Height 400 -FontSize 9 -Name "lblTip" | Out-Null

    $form.HasModule = $true
    $originalName = $form.Name
    $module = $form.Module
    $module.AddFromString(@"
Option Compare Database
Option Explicit

Private Sub cmdCasesByImm_Click()
    OpenCasesByIMM
End Sub

Private Sub cmdSummaryByImm_Click()
    OpenSummaryByIMM
End Sub

Private Sub cmdWorkbench_Click()
    OpenWorkbench
End Sub

Private Sub cmdFindCase_Click()
    FindCaseByIMM
End Sub

Private Sub cmdFindSummary_Click()
    FindSummaryByIMM
End Sub

Private Sub cmdCasesMostDockets_Click()
    OpenCasesMostDockets
End Sub

Private Sub cmdSummaryMostDockets_Click()
    OpenSummaryMostDockets
End Sub

Private Sub cmdYearFilter_Click()
    DoCmd.OpenForm "frmLotDYearFilter"
End Sub

Private Sub cmdCityFilter_Click()
    DoCmd.OpenForm "frmLotDCityFilter"
End Sub

Private Sub cmdCaseDetail_Click()
    DoCmd.OpenForm "frmLotDCaseLookup"
End Sub
"@)
    $AccessApp.DoCmd.Save($acForm, $originalName)
    $AccessApp.DoCmd.Close($acForm, $originalName)
    if ($originalName -ne "frmLotDHome") {
        $AccessApp.DoCmd.Rename("frmLotDHome", $acForm, $originalName)
    }
}

function Build-CaseBrowserForm {
    param($AccessApp)

    $form = $AccessApp.CreateForm()
    $form.RecordSource = "qryWorkbench"
    $form.DefaultView = 1
    $form.AllowAdditions = $false
    $form.AllowEdits = $false
    $form.AllowDeletions = $false
    $form.NavigationButtons = $true
    $form.RecordSelectors = $true
    $form.Caption = "LotD Case Browser"
    $form.Width = 17000
    $form.Section($acDetail).Height = 2200

    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "IMM_NUMBER" -LabelText "IMM Number" -Left 400 -Top 250 -LabelWidth 1300 -TextWidth 1900 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "NAME" -LabelText "Name" -Left 4200 -Top 250 -LabelWidth 900 -TextWidth 6200 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "YEAR" -LabelText "Year" -Left 400 -Top 700 -LabelWidth 1300 -TextWidth 1200 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "CITY_FILED" -LabelText "City" -Left 2600 -Top 700 -LabelWidth 900 -TextWidth 1800 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "CLASS" -LabelText "Class" -Left 5200 -Top 700 -LabelWidth 900 -TextWidth 1800 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "TRACK" -LabelText "Track" -Left 7800 -Top 700 -LabelWidth 900 -TextWidth 2400 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "DOC_COUNT" -LabelText "Docs" -Left 11100 -Top 700 -LabelWidth 900 -TextWidth 1000 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "FIRST_DOC_DT" -LabelText "First Doc" -Left 400 -Top 1150 -LabelWidth 1300 -TextWidth 1500 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "LAST_DOC_DT" -LabelText "Last Doc" -Left 2600 -Top 1150 -LabelWidth 900 -TextWidth 1500 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "MAX_RE_NO" -LabelText "Max RE No" -Left 4700 -Top 1150 -LabelWidth 1100 -TextWidth 1200 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "DOCKET_ROWS_WITH_DOCNO" -LabelText "DocNo Rows" -Left 6500 -Top 1150 -LabelWidth 1300 -TextWidth 1200 | Out-Null

    $originalName = $form.Name
    $AccessApp.DoCmd.Save($acForm, $originalName)
    $AccessApp.DoCmd.Close($acForm, $originalName)
    if ($originalName -ne "frmLotDCaseBrowser") {
        $AccessApp.DoCmd.Rename("frmLotDCaseBrowser", $acForm, $originalName)
    }
}

function Build-CaseDetailForm {
    param($AccessApp)

    $form = $AccessApp.CreateForm()
    $form.RecordSource = "qryWorkbench"
    $form.DefaultView = 0
    $form.AllowAdditions = $false
    $form.AllowEdits = $false
    $form.AllowDeletions = $false
    $form.NavigationButtons = $true
    $form.RecordSelectors = $false
    $form.Caption = "LotD Case Detail"
    $form.Width = 18000
    $form.Section($acDetail).Height = 5200

    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "IMM_NUMBER" -LabelText "IMM Number" -Left 400 -Top 250 -LabelWidth 1400 -TextWidth 2200 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "NAME" -LabelText "Name" -Left 400 -Top 700 -LabelWidth 1400 -TextWidth 12000 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "YEAR" -LabelText "Year" -Left 400 -Top 1150 -LabelWidth 1400 -TextWidth 1000 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "DATE_FILED" -LabelText "Date Filed" -Left 2600 -Top 1150 -LabelWidth 1200 -TextWidth 1500 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "CITY_FILED" -LabelText "City Filed" -Left 5000 -Top 1150 -LabelWidth 1200 -TextWidth 1800 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "CLASS" -LabelText "Class" -Left 7600 -Top 1150 -LabelWidth 900 -TextWidth 2000 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "TRACK" -LabelText "Track" -Left 10400 -Top 1150 -LabelWidth 900 -TextWidth 2600 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "DOC_COUNT" -LabelText "Doc Count" -Left 400 -Top 1600 -LabelWidth 1400 -TextWidth 1200 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "FIRST_DOC_DT" -LabelText "First Doc Date" -Left 2600 -Top 1600 -LabelWidth 1200 -TextWidth 1600 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "LAST_DOC_DT" -LabelText "Last Doc Date" -Left 5000 -Top 1600 -LabelWidth 1200 -TextWidth 1600 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "MAX_RE_NO" -LabelText "Max RE No" -Left 7600 -Top 1600 -LabelWidth 1000 -TextWidth 1200 | Out-Null
    Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "DOCKET_ROWS_WITH_DOCNO" -LabelText "DocNo Rows" -Left 9800 -Top 1600 -LabelWidth 1100 -TextWidth 1200 | Out-Null
    $nature = Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "NATURE" -LabelText "Nature" -Left 400 -Top 2100 -LabelWidth 1400 -TextWidth 15000 -Height 900
    $nature.EnterKeyBehavior = $true
    $nature.ScrollBars = 2
    $source = Add-BoundField -AccessApp $AccessApp -Form $form -FieldName "SOURCE_URL" -LabelText "Source URL" -Left 400 -Top 3200 -LabelWidth 1400 -TextWidth 15000 -Height 900
    $source.EnterKeyBehavior = $true
    $source.ScrollBars = 2

    $originalName = $form.Name
    $AccessApp.DoCmd.Save($acForm, $originalName)
    $AccessApp.DoCmd.Close($acForm, $originalName)
    if ($originalName -ne "frmLotDCaseDetail") {
        $AccessApp.DoCmd.Rename("frmLotDCaseDetail", $acForm, $originalName)
    }
}

function Build-YearFilterForm {
    param($AccessApp)

    $form = $AccessApp.CreateForm()
    $form.RecordSelectors = $false
    $form.NavigationButtons = $false
    $form.DividingLines = $false
    $form.ScrollBars = 0
    $form.Caption = "Filter Cases by Year"
    $form.Width = 9000
    $form.Section($acDetail).Height = 2600
    $form.AllowAdditions = $false
    $form.AllowDeletions = $false
    $form.AllowEdits = $false

    Add-Label -AccessApp $AccessApp -Form $form -Caption "Enter a year and open the filtered case browser." -Left 400 -Top 300 -Width 7500 -Height 350 -FontSize 11 -Bold $true | Out-Null
    Add-Label -AccessApp $AccessApp -Form $form -Caption "Year" -Left 500 -Top 900 -Width 1000 -Height 300 -FontSize 9 -Bold $true | Out-Null
    $textbox = Add-Textbox -AccessApp $AccessApp -Form $form -Name "txtYear" -Left 1600 -Top 850 -Width 1800 -Height 320 -ControlTipText "Enter a 4-digit year, such as 2019."
    $textbox.InputMask = "0000"
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdOpenYearBrowser" -Caption "Open Matching Cases" -Left 3800 -Top 820 -Width 2200 -Height 400 -ControlTipText "Open the case browser filtered to the year you entered." | Out-Null

    $form.HasModule = $true
    $originalName = $form.Name
    $module = $form.Module
    $module.AddFromString(@"
Option Compare Database
Option Explicit

Private Sub cmdOpenYearBrowser_Click()
    Dim yearValue As String
    yearValue = Trim(Nz(Me.txtYear, ""))
    If yearValue = "" Then
        MsgBox "Enter a year first.", vbInformation
        Exit Sub
    End If
    DoCmd.OpenForm "frmLotDCaseBrowser", , , "[YEAR]='" & Replace(yearValue, "'", "''") & "'"
End Sub
"@)
    $AccessApp.DoCmd.Save($acForm, $originalName)
    $AccessApp.DoCmd.Close($acForm, $originalName)
    if ($originalName -ne "frmLotDYearFilter") {
        $AccessApp.DoCmd.Rename("frmLotDYearFilter", $acForm, $originalName)
    }
}

function Build-CityFilterForm {
    param($AccessApp)

    $form = $AccessApp.CreateForm()
    $form.RecordSelectors = $false
    $form.NavigationButtons = $false
    $form.DividingLines = $false
    $form.ScrollBars = 0
    $form.Caption = "Filter Cases by City"
    $form.Width = 11000
    $form.Section($acDetail).Height = 2600
    $form.AllowAdditions = $false
    $form.AllowDeletions = $false
    $form.AllowEdits = $false

    Add-Label -AccessApp $AccessApp -Form $form -Caption "Enter a city name or part of a city name." -Left 400 -Top 300 -Width 8500 -Height 350 -FontSize 11 -Bold $true | Out-Null
    Add-Label -AccessApp $AccessApp -Form $form -Caption "City" -Left 500 -Top 900 -Width 1000 -Height 300 -FontSize 9 -Bold $true | Out-Null
    Add-Textbox -AccessApp $AccessApp -Form $form -Name "txtCity" -Left 1600 -Top 850 -Width 3200 -Height 320 -ControlTipText "Enter a city such as Toronto or Ottawa." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdOpenCityBrowser" -Caption "Open Matching Cases" -Left 5100 -Top 820 -Width 2200 -Height 400 -ControlTipText "Open the case browser filtered to the city you entered." | Out-Null

    $form.HasModule = $true
    $originalName = $form.Name
    $module = $form.Module
    $module.AddFromString(@"
Option Compare Database
Option Explicit

Private Sub cmdOpenCityBrowser_Click()
    Dim cityValue As String
    cityValue = Trim(Nz(Me.txtCity, ""))
    If cityValue = "" Then
        MsgBox "Enter a city first.", vbInformation
        Exit Sub
    End If
    DoCmd.OpenForm "frmLotDCaseBrowser", , , "[CITY_FILED] LIKE '*" & Replace(cityValue, "'", "''") & "*'"
End Sub
"@)
    $AccessApp.DoCmd.Save($acForm, $originalName)
    $AccessApp.DoCmd.Close($acForm, $originalName)
    if ($originalName -ne "frmLotDCityFilter") {
        $AccessApp.DoCmd.Rename("frmLotDCityFilter", $acForm, $originalName)
    }
}

function Build-CaseLookupForm {
    param($AccessApp)

    $form = $AccessApp.CreateForm()
    $form.RecordSelectors = $false
    $form.NavigationButtons = $false
    $form.DividingLines = $false
    $form.ScrollBars = 0
    $form.Caption = "Open Single Case Detail"
    $form.Width = 11000
    $form.Section($acDetail).Height = 2800
    $form.AllowAdditions = $false
    $form.AllowDeletions = $false
    $form.AllowEdits = $false

    Add-Label -AccessApp $AccessApp -Form $form -Caption "Enter an exact IMM number to open one case detail record." -Left 400 -Top 300 -Width 9000 -Height 350 -FontSize 11 -Bold $true | Out-Null
    Add-Label -AccessApp $AccessApp -Form $form -Caption "IMM Number" -Left 500 -Top 950 -Width 1200 -Height 300 -FontSize 9 -Bold $true | Out-Null
    Add-Textbox -AccessApp $AccessApp -Form $form -Name "txtIMM" -Left 1900 -Top 900 -Width 2600 -Height 320 -ControlTipText "Enter an exact IMM number, such as IMM-10085-12." | Out-Null
    Add-Button -AccessApp $AccessApp -Form $form -Name "cmdOpenCaseDetail" -Caption "Open Case Detail" -Left 4900 -Top 870 -Width 2100 -Height 400 -ControlTipText "Open a single-case detail form for the IMM number you entered." | Out-Null

    $form.HasModule = $true
    $originalName = $form.Name
    $module = $form.Module
    $module.AddFromString(@"
Option Compare Database
Option Explicit

Private Sub cmdOpenCaseDetail_Click()
    Dim immValue As String
    immValue = Trim(Nz(Me.txtIMM, ""))
    If immValue = "" Then
        MsgBox "Enter an IMM number first.", vbInformation
        Exit Sub
    End If
    DoCmd.OpenForm "frmLotDCaseDetail", , , "[IMM_NUMBER]='" & Replace(immValue, "'", "''") & "'"
End Sub
"@)
    $AccessApp.DoCmd.Save($acForm, $originalName)
    $AccessApp.DoCmd.Close($acForm, $originalName)
    if ($originalName -ne "frmLotDCaseLookup") {
        $AccessApp.DoCmd.Rename("frmLotDCaseLookup", $acForm, $originalName)
    }
}

if (-not (Test-Path $CasesCsv)) {
    throw "Cases CSV not found: $CasesCsv"
}
if (-not (Test-Path $SummaryCsv)) {
    throw "Summary CSV not found: $SummaryCsv"
}

$outputDirectory = Split-Path -Parent $OutputPath
if (-not (Test-Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory | Out-Null
}
if (Test-Path $OutputPath) {
    Remove-Item $OutputPath -Force
}

$access = New-Object -ComObject Access.Application
try {
    $access.Visible = $false
    $access.NewCurrentDatabase((Resolve-Path $outputDirectory).Path + "\" + (Split-Path -Leaf $OutputPath))
    $access.DoCmd.SetWarnings($false)

    $access.DoCmd.TransferText($acImportDelim, "", "Cases", (Resolve-Path $CasesCsv).Path, $true)
    $access.DoCmd.TransferText($acImportDelim, "", "DocketSummary", (Resolve-Path $SummaryCsv).Path, $true)

    $db = $access.CurrentDb()
    $db.Execute("CREATE INDEX idx_Cases_IMM_NUMBER ON Cases (IMM_NUMBER)")
    $db.Execute("CREATE INDEX idx_Cases_YEAR ON Cases (YEAR)")
    $db.Execute("CREATE INDEX idx_DocketSummary_IMM_NUMBER ON DocketSummary (IMM_NUMBER)")
    $db.Execute("CREATE INDEX idx_DocketSummary_YEAR ON DocketSummary (YEAR)")
    $db.Execute("CREATE INDEX idx_DocketSummary_DOC_COUNT ON DocketSummary (DOC_COUNT)")

    $queries = @{
        "qryCases_ByIMM" = "SELECT * FROM Cases ORDER BY IMM_NUMBER;"
        "qryDocketSummary_ByIMM" = "SELECT * FROM DocketSummary ORDER BY IMM_NUMBER;"
        "qryCases_MostDockets" = "SELECT * FROM Cases ORDER BY DOC_COUNT DESC, IMM_NUMBER;"
        "qryDocketSummary_MostDockets" = "SELECT * FROM DocketSummary ORDER BY DOC_COUNT DESC, IMM_NUMBER;"
        "qryFindCaseByIMM" = "SELECT * FROM Cases WHERE IMM_NUMBER LIKE [Enter IMM number or prefix:] & '*' ORDER BY IMM_NUMBER;"
        "qryFindSummaryByIMM" = "SELECT * FROM DocketSummary WHERE IMM_NUMBER LIKE [Enter IMM number or prefix:] & '*' ORDER BY IMM_NUMBER;"
        "qryWorkbench" = "SELECT c.IMM_NUMBER, c.NAME, c.YEAR, c.DATE_FILED, c.CITY_FILED, c.NATURE, c.CLASS, c.TRACK, c.DOC_COUNT, s.FIRST_DOC_DT, s.LAST_DOC_DT, s.MAX_RE_NO, s.DOCKET_ROWS_WITH_DOCNO FROM Cases AS c INNER JOIN DocketSummary AS s ON c.IMM_NUMBER = s.IMM_NUMBER ORDER BY c.IMM_NUMBER;"
    }

    foreach ($name in $queries.Keys) {
        $db.CreateQueryDef($name, $queries[$name]) | Out-Null
    }

    Add-VbaModule -AccessApp $access
    Build-CaseBrowserForm -AccessApp $access
    Build-CaseDetailForm -AccessApp $access
    Build-YearFilterForm -AccessApp $access
    Build-CityFilterForm -AccessApp $access
    Build-CaseLookupForm -AccessApp $access
    Build-HomeForm -AccessApp $access

    try {
        $access.SetOption("Display Form", "frmLotDHome")
    } catch {
        try {
            $access.SetOption("Display Form/Page", "frmLotDHome")
        } catch {
        }
    }

    $db.TableDefs("Cases").Properties.Append($db.TableDefs("Cases").CreateProperty("Description", 10, "One row per IMM file. Use datasheet filters or qryFindCaseByIMM for quick lookup."))
    $db.TableDefs("DocketSummary").Properties.Append($db.TableDefs("DocketSummary").CreateProperty("Description", 10, "One row per IMM file with docket date range and count summary. Full dockets remain in PostgreSQL lotd.access_dockets."))

    $db.Close()
    $access.CloseCurrentDatabase()
}
finally {
    if ($null -ne $access) {
        $access.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($access) | Out-Null
    }
}

Write-Output "access_frontend=$((Resolve-Path $OutputPath).Path)"