    # Brian's Brain Cellular Automaton

    This project simulates Brian's Brain, a 2D cellular automaton with three cell states: OFF (0), ON (1), and DYING (2).

    ## Project Structure

    - `main.py` - Command line interface and simulation orchestration
    - `brain.py` - Core simulation logic and BriansBrain class
    - `test_brain.py` - Unit tests for the simulation logic
    - `sample_seed.txt` - Example seed file with ON and DYING states

    ## How to Run

    ```
    python3 main.py --seed-file sample_seed.txt --generations 200 --width 40 --height 20 --output-dir output
    ```

    Or generate a random seed:

    ```
    python3 main.py --random-seed 42 --generations 200 --width 40 --height 20 --output-dir output
    ```

    ## Running Tests

    ```
    python3 test_brain.py
    ```

    ## Features

    - **Separated concerns**: Core logic in `brain.py`, CLI in `main.py`
    - **State 2 support**: Seed files can include DYING cells (state 2)
    - **ANSI animation**: Smooth terminal animation using ANSI escape codes
    - **External constants**: SYMBOLS and state constants are easily configurable
    - **Unit tests**: Basic test coverage for core functionality

    ## Seed File Format

    - Each line is a row in the grid
    - Use '0' for OFF cells, '1' for ON cells, '2' for DYING cells
    - The pattern will be centered in the grid

    Example (`sample_seed.txt`):
    ```
    00000
    00100
    00010
    01210
    00000
    ```

    ## Controls
    - Press `Ctrl+C` to stop the simulation early

    ## Requirements
    - Python 3.6 or higher (no external dependencies) 