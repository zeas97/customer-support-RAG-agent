# Knowledge Base Data
PRODUCTS = [
    {
        "name": "UltraPhone X",
        "price": "$799",
        "features": "6.5\" OLED display, 128GB storage, 12MP camera, Face Recognition",
        "colors": "Black, Silver, Blue",
        "availability": "In stock",
        "warranty": "1-year limited warranty",
    },
    {
        "name": "PowerBook Pro",
        "price": "$1299",
        "features": "15.6\" Retina display, 512GB SSD, 16GB RAM, Intel i7 processor",
        "colors": "Space Gray, Silver",
        "availability": "In stock",
        "warranty": "2-year limited warranty",
    },
    {
        "name": "SmartWatch Elite",
        "price": "$349",
        "features": "Heart rate monitor, GPS, 2-day battery life, Water resistant",
        "colors": "Black, White, Red",
        "availability": "Limited stock",
        "warranty": "1-year limited warranty",
    },
    {
        "name": "AudioPods Max",
        "price": "$199",
        "features": "Noise cancellation, 24-hour battery life, Touch controls",
        "colors": "White, Black",
        "availability": "In stock",
        "warranty": "1-year limited warranty",
    },
    {
        "name": "HomeAssist Speaker",
        "price": "$129",
        "features": "Voice assistant, Room-filling sound, Smart home controls",
        "colors": "Charcoal, Sand",
        "availability": "In stock",
        "warranty": "1-year limited warranty",
    },
]

POLICIES = [
    {
        "type": "Shipping Policy",
        "content": (
            "Standard shipping (3-5 business days): $4.99\n"
            "Express shipping (1-2 business days): $12.99\n"
            "Free standard shipping on orders over $50\n"
            "International shipping available to select countries for additional fee\n"
            "Currently not shipping to P.O. boxes"
        ),
    },
    {
        "type": "Return Policy",
        "content": (
            "30-day return period for unused items in original packaging\n"
            "Return shipping is free for defective products\n"
            "15% restocking fee may apply for opened items\n"
            "Gift receipts allow returns for store credit only\n"
            "Special order items are non-returnable"
        ),
    },
    {
        "type": "Warranty Policy",
        "content": (
            "All electronics come with manufacturer's warranty\n"
            "Extended protection plans available at checkout\n"
            "Warranty does not cover accidental damage or water damage\n"
            "Proof of purchase required for warranty service\n"
            "Warranty is void if product is modified or repaired by unauthorized persons"
        ),
    },
    {
        "type": "Payment Options",
        "content": (
            "All major credit cards accepted\n"
            "PaySecure digital wallet\n"
            "Installment payment plans available on purchases over $300\n"
            "Store credit and gift cards\n"
            "No checks or money orders accepted"
        ),
    },
    {
        "type": "Privacy Policy",
        "content": (
            "Customer information is never sold to third parties\n"
            "Opt-in required for marketing communications\n"
            "Data is stored securely using industry-standard encryption\n"
            "Customers can request deletion of personal information\n"
            "See full privacy policy at company website"
        ),
    },
]


def get_knowledge_base_data():
    """
    Returns the lists/dicts for products and policies.
    You can add more logic here if needed, such as dynamic construction
    of the knowledge base from multiple sources.
    """
    return PRODUCTS, POLICIES
