import streamlit as st

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Ticket Booking System")

st.write("Book your movie tickets easily.")

movies = {
    "Avengers: Endgame": 180,
    "Spider-Man": 160,
    "The Lion King": 140,
    "Interstellar": 200,
    "Inside Out": 130
}

ticket_types = {
    "Regular": 0,
    "Premium": 50,
    "VIP": 100
}

st.subheader("🎟️ Booking Details")

movie = st.selectbox(
    "Select Movie",
    list(movies.keys())
)

tickets = st.number_input(
    "Number of Tickets",
    min_value=1,
    max_value=20,
    value=1
)

ticket_type = st.selectbox(
    "Select Ticket Type",
    list(ticket_types.keys())
)

base_price = movies[movie]

extra_price = ticket_types[ticket_type]

price_per_ticket = base_price + extra_price

total = price_per_ticket * tickets

st.divider()

st.subheader("💳 Price Details")

st.write(f"Movie base price: ₹{base_price}")

st.write(
    f"{ticket_type} category extra: ₹{extra_price}"
)

st.write(
    f"Price per ticket: ₹{price_per_ticket}"
)

st.write(
    f"Number of tickets: {tickets}"
)

if st.button(
    "🎟️ Confirm Booking",
    use_container_width=True
):

    st.success(
        "Booking confirmed successfully! 🎉"
    )

    st.markdown("### 📋 Booking Summary")

    st.write(f"**Movie:** {movie}")

    st.write(
        f"**Ticket Type:** {ticket_type}"
    )

    st.write(
        f"**Tickets:** {tickets}"
    )

    st.success(
        f"### 💰 Total Price: ₹{total:.2f}"
    )

st.caption("Enjoy your movie! 🍿")