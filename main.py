from fastapi import FastAPI
import uvicorn
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.product_price import switch_on

app = FastAPI()



@app.post("/product-price")
async def get_product_price(request: dict):
  product_url = request["productUrl"]
  product_seller = product_url.split(".")[1]
  final_price = switch_on(product_seller, product_url)

  if final_price:
      return JSONResponse(content={"product_seller": "found", "final_price": final_price})
  else:
      return JSONResponse(content={"product_seller": "not found"})
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)