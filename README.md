# Abstract Puzzle Generator

This program generates and displays abstract puzzles on the terminal.

## Running the Program

To run the program, navigate to its directory in your terminal and use Python:

```bash
python main.py [width] [height] [delay] [count] [rule_id]
```

All arguments are optional and positional. If arguments are omitted, the program will use default values, which are likely defined in the `argv_helper.py` script. The order of arguments matters.

### Arguments

1.  `width` (integer)
    *   **Purpose**: Specifies the width of the puzzle.
    *   **Behavior**:
        *   If `count` (argument 4) is positive: This value is used as the **exact width** for each generated puzzle.
        *   If `count` is zero or negative (continuous mode): This value serves as the **maximum width** for randomly sized puzzles.
    *   **Example**: `10`

2.  `height` (integer)
    *   **Purpose**: Specifies the height of the puzzle.
    *   **Behavior**:
        *   If `count` (argument 4) is positive: This value is used as the **exact height** for each generated puzzle.
        *   If `count` is zero or negative (continuous mode): This value serves as the **maximum height** for randomly sized puzzles. Note that in continuous mode, the random height will also be constrained to be less than or equal to the random width chosen for that specific puzzle.
    *   **Example**: `8`

3.  `delay` (float)
    *   **Purpose**: Sets an animation delay in seconds. This delay is used between printing different components or stages of the puzzle, allowing for a visual progression.
    *   **Example**: `0.1` for a fast animation, `0.5` for a slower one.

4.  `count` (integer)
    *   **Purpose**: Determines the number of puzzles to generate.
    *   **Behavior**:
        *   **Positive value (e.g., `5`)**: Generates exactly this many puzzles. Each puzzle will adhere to the `width`, `height`, and `rule_id` specified in the arguments.
        *   **Zero or negative value (e.g., `0` or `-1`)**: Activates continuous generation mode. Puzzles are generated indefinitely until the program is manually stopped.
            *   In this mode, the `width` and `height` arguments define the *maximums* for random puzzle dimensions.
            *   The `rule_id` argument (argument 5) is ignored, and a random connection rule is selected for each new puzzle.
    *   **Example**: `3` (to generate 3 puzzles), `0` (to run in continuous mode).

5.  `rule_id` (integer or identifier)
    *   **Purpose**: Specifies the connection logic (referred to as "opposite key" rule) that dictates how puzzle pieces fit together. The program internally maps this ID to a specific set of rules. The ID of the active rule is printed to the console after each puzzle is generated.
    *   **Behavior**:
        *   This argument is only effective if `count` (argument 4) is a positive number.
        *   If `count` is zero or negative (continuous mode), this argument is disregarded, and a random rule is chosen for each puzzle.
    *   **Example**: `1` (The set of valid IDs depends on the `OPPOSITE_KEYS` and `OPPOSITE_PIECE_KEY_DIGITS` definitions within the program's code. To discover available rule IDs, you can run the program in continuous mode and observe the rule IDs printed with each puzzle.)

### Usage Examples

*   **Generate 1 puzzle of size 10x7 with a 0.2-second delay, using connection rule ID 0:**
    ```bash
    python main.py 10 7 0.2 1 0
    ```

*   **Generate puzzles continuously. Puzzles will have random dimensions up to a maximum of 15x10. Use a 0.1s delay. Connection rules will be randomized for each puzzle:**
    ```bash
    python main.py 15 10 0.1 0
    ```
    *(In this example, `0` for the `count` argument enables continuous mode. The `rule_id` could be omitted or set to any value, as it will be ignored.)*

*   **Run with all default settings (assuming `argv_helper.py` provides defaults for all arguments if none are specified):**
    ```bash
    python main.py
    ```
    *(This would likely run in continuous mode if the default value for `count` is 0 or negative.)*