import time
import asyncio
from asyncio import Queue

class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        print(f"The Cashier_{cashier_number} "
              f"will checkout Customer_{customer.customer_id}")
        
        for product in customer.products:
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product_{product.product_name} "
                  f"in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
        
        print(f"The Cashier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id} "
              f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")
        
        queue.task_done()

def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)


async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count + customers)]
        
        for customer in customers:
            print("Waiting to put customer in line....")
            await queue.put(customer)
            print("Customer put in line...")
        
        customer_count = customer_count + len(customers)
        await asyncio.sleep(0.001)
        return customer_count

async def main():
    customer_queue = Queue(5)
    customers_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, 10))
    cashiers = [checkout_customer(customer_queue, i) for i in range(4)]
    
    await asyncio.gather(customer_producer, *cashiers)
    print(f"The supermarket process finished "
          f"{customer_producer.result()} customers "
                f"in {round(time.perf_counter() - customers_start_time, ndigits=2)} secs")

if __name__ == "__main__":
    asyncio.run(main())
# +--------|------------|-----------|-----------------------|-------------------------    
# Queue    | Customer   | Cashier   |  Time each Customer   |  Time for all Customers
# 2        | 2          | 2         |     ~ 2.03            |     2.03      
# 2        | 3          | 2         |     ~ 2.04            |     4.07                                            
# 2        | 4          | 2         |     ~ 2.02            |     4.06      
# 2        | 10         | 3         |     ~ 2.03            |     10.14      
# 5        | 10         | 4         |     ~ 2.02            |     6.09          
# 5        | 20         | 5         |     ~ 2.04            |     8.14
# +--------|------------|-----------|-----------------------|-------------------------