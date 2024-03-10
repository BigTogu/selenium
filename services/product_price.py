from services.selenium_service import get_price_from_url

SELECTORS = {
    "mediamarkt": {
        "DENY_BTN": ".sc-4615157e-13.hPIYBS [data-test='pwa-consent-layer-deny-all']",
        "PRICE": ".sc-a2b334e5-0",
    },
    "elcorteingles": {
        "DENY_BTN": "#onetrust-reject-all-handler",
        "PRICE": ".product_detail-aside--price_color_selector",
    },
    "aliexpress": {
        "DENY_BTN": ".btn-accept",
        "PRICE": ".es--wrap--erdmPRe",
    },
    "pccomponentes": {
        "DENY_BTN": "#cookiesrejectAll",
        "PRICE": "#pdp-price-current-integer",
    },
}


def get_product_price(product_url, selectors):
    try:
        product_price = get_price_from_url(
            product_url,
            selectors["DENY_BTN"],
            selectors["PRICE"],
            selectors["PRICE"],
        )
        print(product_price, "--------product_price")
        return product_price
    except Exception as error:
        print("Error al obtener el precio del producto:", error)
        return None


def switch_on(product_seller, product_url):
    selectors = SELECTORS.get(product_seller)

    if not selectors:
        print("Vendedor no válido:", product_seller)
        return None

    if product_seller == "mediamarkt":
        return get_product_price(product_url, selectors)
    elif product_seller in ["elcorteingles", "aliexpress", "pccomponentes"]:
        return get_product_price(product_url, selectors)
    else:
        return None
