from enum import Enum


class EquasionType(Enum):
    EQUALITY = 1
    LESS = 2
    LESS_OR_EQUAL = 3
    GREATER = 4
    GREATER_OR_EQUAL = 5
    APPROXIMATION = 6
    SIGNIFICANTLY_LESS = 7
    SIGNIFICANTLY_GREATER = 8
    OTHER = 9

    def to_string(self) -> str:
        if self == EquasionType.EQUALITY:
            return 'equals'
        if self == EquasionType.LESS:
            return 'less'
        if self == EquasionType.LESS_OR_EQUAL:
            return 'less or equal'
        if self == EquasionType.GREATER:
            return 'greater'
        if self == EquasionType.GREATER_OR_EQUAL:
            return 'greater or equal'
        if self == EquasionType.APPROXIMATION:
            return 'approximates'
        if self == EquasionType.SIGNIFICANTLY_LESS:
            return 'significantly less'
        if self == EquasionType.SIGNIFICANTLY_GREATER:
            return 'significantly greater'
        return ''


def get_equasion_type_from_string(string: str) -> EquasionType:
    if string == 'equals':
        return EquasionType.EQUALITY
    if string == 'less':
        return EquasionType.LESS
    if string == 'less or equal':
        return EquasionType.LESS_OR_EQUAL
    if string == 'greater':
        return EquasionType.GREATER
    if string == 'greater or equal':
        return EquasionType.GREATER_OR_EQUAL
    if string == 'approximates':
        return EquasionType.APPROXIMATION
    if string == 'significantly less':
        return EquasionType.SIGNIFICANTLY_LESS
    if string == 'significantly greater':
        return EquasionType.SIGNIFICANTLY_GREATER
    return EquasionType.OTHER


if __name__ == '__main__':
    eqt = EquasionType.EQUALITY
    print(eqt.to_string())
