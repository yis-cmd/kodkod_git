class GoBack(Exception):
    pass


class DuplicateIDError(Exception):
    # ID must be unique
    pass


class IDNotExistsError(Exception):
    pass


class DuplicatedDutiesForIDError(Exception):
    # One soldier can only have one of each type of duties
    pass


class DutyNotExistsForIDError(Exception):
    # The soldier doesn't have this duty
    pass


class DutyTypeNotExistsError(Exception):
    pass


class DutyTypeAlreadyExistsError(Exception):
    pass


class InvalidDayError(Exception):
    pass
