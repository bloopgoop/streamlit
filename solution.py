import random
import streamlit as st

MAX_A = 10
MAX_X = 10
MAX_B = 20


def generate_equation():
    """Generate a linear equation ax + b = c with integer solution."""
    # First choose the solution (x) as an integer
    x = random.randint(-MAX_X, MAX_X)

    # Choose coefficient 'a' (non-zero)
    a = random.randint(1, MAX_A)
    if random.choice([True, False]):
        a = -a  # 50% chance of negative coefficient

    # Choose 'b'
    b = random.randint(-MAX_B, MAX_B)

    # Calculate 'c' to ensure the equation ax + b = c has our chosen x as solution
    c = a * x + b

    return a, b, c, x


def format_equation(a, b, c):
    """Format the equation ax + b = c in a readable way."""
    equation = ""

    # Format ax term
    if a == 1:
        equation += "x"
    elif a == -1:
        equation += "-x"
    else:
        equation += f"{a}x"

    # Format b term
    if b > 0:
        equation += f" + {b}"
    elif b < 0:
        equation += f" - {abs(b)}"
    # If b is 0, we don't add anything

    # Add equals sign and c
    equation += f" = {c}"

    return equation


def main():
    st.set_page_config(page_title="Linear Equation Practice")

    st.title("Linear Equation Practice")
    st.write("Solve for x in the following equation:")

    # Initialize session state to store equation variables if they don't exist
    if "a" not in st.session_state:
        (
            st.session_state.a,
            st.session_state.b,
            st.session_state.c,
            st.session_state.solution,
        ) = generate_equation()

    # Display the equation
    equation = format_equation(
        st.session_state.a, st.session_state.b, st.session_state.c
    )
    st.subheader(equation)

    # Input for student's answer
    student_answer = st.number_input("Your answer (x = ?)", step=1, value=0)

    if st.button("New Equation"):
        (
            st.session_state.a,
            st.session_state.b,
            st.session_state.c,
            st.session_state.solution,
        ) = generate_equation()
        st.rerun()

    if st.button("Check Answer"):
        if student_answer == st.session_state.solution:
            message = "Correct. "

            # b_hint
            if st.session_state.b > 0:
                message += f"Subtracting {st.session_state.b} to each side and "
            if st.session_state.b < 0:
                message += f"Adding {abs(st.session_state.b)} to each side and "

            # a_hint
            a_hint = f"dividing both sides by {st.session_state.a} "
            if st.session_state.b == 0:
                a_hint = a_hint.capitalize()

            message += a_hint
            message += f"gives x = {st.session_state.solution}"

            st.success(message)
            st.balloons()
        else:
            message = "Incorrect. You should "

            # b_hint
            if st.session_state.b > 0:
                message += f"subtract {st.session_state.b} to both sides and then "
            if st.session_state.b < 0:
                message += f"add {abs(st.session_state.b)} to both sides and then "

            # a_hint
            message += f"divide {st.session_state.a} from both sides."

            st.error(message)


if __name__ == "__main__":
    main()
