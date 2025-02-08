import streamlit as st

def decision_flow():
    st.title("HU IP PFR Decision Helper")
    
    # Step 1: Determine their range
    range_input = st.radio("What is their range?", ["Uncapped", "Capped"])
    
    if range_input == "Uncapped":
        fast_play = st.radio("Do they fast play their strong stuff?", ["Yes", "No"])
        if fast_play == "Yes":
            value_bet = "Bet Small"
            sdv_bet = "Bet Small (Flop), Check (Turn, River)"
            bluff_bet = "Bet Small (Flop, Turn), Bet Medium (River)"
        else:
            value_bet = "Bet Big"
            sdv_bet = "Check"
            bluff_bet = "Check (Flop, Turn), Bet Small (River)"
    
    elif range_input == "Capped":
        inelastic = st.radio("Do they have inelastic hands?", ["Yes", "No"])
        if inelastic == "Yes":
            value_bet = "Bet Big"
            sdv_bet = "Check"
            bluff_bet = "Bet Big (Turn), Bet Small (River)"
        else:
            value_bet = "Bet Small"
            sdv_bet = "Check"
            bluff_bet = "Bet Small (Turn), Bet Big (River)"
    
    # Step 3: Determine our hand type
    hand_type = st.radio("What is our hand?", ["Value", "SDV", "Bluff"])
    
    if hand_type == "Value":
        st.subheader(f"Suggested Play: {value_bet}")
    elif hand_type == "SDV":
        st.subheader(f"Suggested Play: {sdv_bet}")
    elif hand_type == "Bluff":
        st.subheader(f"Suggested Play: {bluff_bet}")
    
    if st.button("Restart"):
        st.experimental_rerun()

if __name__ == "__main__":
    decision_flow()
