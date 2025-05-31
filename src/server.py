import asyncio

from factory.app import app
import uvicorn
# async def run_hyper_corn():
#     import hypercorn.asyncio as server
#     import hypercorn
#     config = hypercorn.Config()
#     config.debug = True
#     config.bind = ["localhost:8090"]
#     await server.serve(app, config=config)

if __name__ == "__main__":
    uvicorn.run("server:app", reload=True, port=8090, host="0.0.0.0", workers=8, timeout_keep_alive=3)
    # asyncio.run(run_hyper_corn())

