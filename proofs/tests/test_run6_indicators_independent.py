"""Full independent ambient audit; intentionally substantial exact certificate."""

from magic_number.run6_indicators_independent import audit_all


def test_all_444624_memberships_with_independent_ambient_equations():
    audit=audit_all(progress=True)
    assert audit["exact_membership_decisions"]==444624
    assert audit["decision_counts"]=={"MIXED":360154,"SIX_ROW":83054,"SPURION":1416}
    assert audit["twistors_independently_nonzero"]==59472
    assert audit["all_indicator_rows_match"]
