from bank import Bank
import streamlit as st

if "branch1" not in st.session_state:
    st.session_state.branch1 = Bank("Mehran", 0)

branch1 = st.session_state.branch1          


# ---------------------------------------------
# Initialize Accounts in Session State
# ---------------------------------------------
if "branch_accounts" not in st.session_state:
    st.session_state.branch_accounts =  []

st.title("🏦 Simple Banking System")
st.write("This is a simple banking system built using Streamlit.")
menu = st.sidebar.selectbox(
    "Select Action",
    ["Open Account", "Check Balance", "Deposit", "Withdraw", "Transfer", "Show All Accounts"]
)

# ----------------------
# Open Account
# ----------------------
if menu == "Open Account":
    st.header("➕ Open a New Account")

    cnic = st.text_input("Enter CNIC")
    title = st.text_input("Account Title")
    deposit = st.number_input("Initial Deposit", min_value=0)

    if st.button("Create Account"):
        acc =branch1.open_account(cnic, title, deposit)
        st.success("Account Created Successfully!")
        st.write(f"**Account Number:** {acc['account_number']}")
        st.write(f"**PIN:** {acc['pin']} (Save this!)")
        
        
    # ----------------------
# Check Balance
# ----------------------
elif menu == "Check Balance":
    st.header("💰 Check Balance")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)

    if st.button("Show Balance"):
        bal,err= branch1.show_balance(acc_no, pin)
        if err:
            st.error(err)
        else:
            st.success(f"Your Current Balance is: Rs {bal}")
# ----------------------
# Deposit
# ----------------------
elif menu == "Deposit":
    st.header("📥 Deposit Amount")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999)
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        bal, err = branch1.deposit_amt(acc_no, amt)
        if err:
            st.error(err)
        else:
            st.success(f"Amount Deposited! New Balance: Rs {bal}")

# ----------------------
# Withdraw
# ----------------------
elif menu == "Withdraw":
    st.header("📤 Withdraw Amount")

    acc_no = st.number_input("Account Number", min_value=1000, max_value=9999)
    pin = st.number_input("PIN", min_value=1000, max_value=9999)
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        bal, err = branch1.withdraw_amt(acc_no, pin, amt)
        if err:
            st.error(err)
        else:
            st.success(f"Withdrawal Successful! New Balance: Rs {bal}")

# ----------------------
# Transfer
# ----------------------
elif menu == "Transfer":
    st.header("💸 Transfer Amount")

    acc_no = st.number_input("Your Account Number", min_value=1000, max_value=9999)
    pin = st.number_input("Your PIN", min_value=1000, max_value=9999)
    amt = st.number_input("Amount", min_value=1)
    ben = st.number_input("Beneficiary Account Number", min_value=1000, max_value=9999)

    if st.button("Transfer"):
        bal, err = branch1.transfer_amt(acc_no, pin, amt, ben)
        if err:
            st.error(err)
        else:
            st.success(f"Transfer Successful! Remaining Balance: Rs {bal}")

# ----------------------
# Show All Accounts
# ----------------------
elif menu == "Show All Accounts":
    st.header("📋 All Accounts (Debug View)")

    if st.button("Show All Accounts"):
        st.write(branch1.show_all_accounts())


