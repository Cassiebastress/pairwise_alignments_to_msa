# Type for pairwise alignment
PWA = tuple[str, str]


def still_has_content(pwas: list[PWA], i: int) -> bool:
    """Return True if any template string has length > i."""
    return any(len(row[0]) > i for row in pwas)


def has_gap_at_position(pwas: list[PWA], i: int) -> bool:
    """Return True if any alignment template has a '-' at position i."""
    return any(len(row[0]) > i and row[0][i] == "-" for row in pwas)


def template_chars_only(my_string):
    return my_string.replace('-', '')


def validate_input(pwas: list[PWA]) -> None:
    # Verify that within each tuple, both sequecnes have the same length
    for template, sequence in pwas:
        if len(template) != len(sequence):
            raise ValueError("Template and sequence must have the same length.")

    if len({template_chars_only(seq) for seq, _ in pwas}) != 1:
        raise ValueError("All reference sequences must be the same")


def aligned_tuples_to_MSA(pwas_input: list[PWA]) -> list[str]:
    """
    Convert a list of single alignments into a multisequence alignment.
    """
    i = 0

    # Convert copy to uppercase
    pwas = [[template.upper(), sequence.upper()] for template, sequence in pwas_input]

    # Validate input
    validate_input(pwas)

    while still_has_content(pwas, i):

        # If there's a gap in any template at position i
        if has_gap_at_position(pwas, i):

            for j, (template, sequence) in enumerate(pwas):

                # If the template has no gap at position i,
                # Insert '-' in both template and sequence at position i
                # to maintain alignment with other templates
                if len(template) > i and template[i] != "-":
                    pwas[j][0] = template[:i] + "-" + template[i:]
                    pwas[j][1] = sequence[:i] + "-" + sequence[i:]

        i += 1

    output = [pwas[0][0]] + [sequence for _, sequence in pwas]

    # Fill the potential gap at the end
    max_length = max(len(seq) for seq in output)
    return [seq + "-" * (max_length - len(seq)) for seq in output]
