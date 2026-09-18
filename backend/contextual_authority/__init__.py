"""Additive contextual authority analysis primitives."""

from .context_units import build_context_units
from .discussion_units import (
	ContinuityComponents,
	DiscussionUnit,
	ParagraphFeatures,
	compute_continuity,
	segment_discussion_units,
)
from .subthemes import ArgumentEvidence, SubTheme, extract_argument_evidence, segment_subthemes
from .models import ChunkInput, ContextUnit, SnapshotSpec
from .observations import ContextObservation, extract_context_observations, extract_segment_observations
from .voting import RuleAgreementReport, RuleVote, build_agreement_report
from .teacher_contract import (
	TeacherBatch,
	TeacherCitation,
	TeacherExample,
	build_teacher_messages,
	estimate_cost_usd,
)

__all__ = [
	"ChunkInput",
	"ContextObservation",
	"ContextUnit",
	"SnapshotSpec",
	"build_context_units",
	"ContinuityComponents",
	"DiscussionUnit",
	"ParagraphFeatures",
	"compute_continuity",
	"segment_discussion_units",
	"ArgumentEvidence",
	"SubTheme",
	"extract_argument_evidence",
	"segment_subthemes",
	"extract_context_observations",
	"extract_segment_observations",
	"RuleAgreementReport",
	"RuleVote",
	"build_agreement_report",
	"TeacherBatch",
	"TeacherCitation",
	"TeacherExample",
	"build_teacher_messages",
	"estimate_cost_usd",
]
