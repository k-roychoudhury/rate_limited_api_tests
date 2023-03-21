r""" scripts.test_attachment_endpoint module """


# importing standard modules ==================================================
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor


# importing third-party modules ===============================================
from requests import (
    Session,
    Response
)


# method definitions ==========================================================
def get_attachments(ucid: str) -> List[Dict[str, Any]]:
    url: str = "http://localhost:8000/api/v1/attachment/list"
    __params: Dict[str, str] = {"ucid": ucid}
    with Session() as session:
        response: Response = session.get(url, params=__params)
    
    data: Dict[str, Any] = response.json()
    num_items: int = int(data.get("items"))
    attachments: List[Dict[str, Any]] = data.get("attachments")
    assert len(attachments) == num_items
    return attachments


def main() -> None:

    num_requests: int = 100

    with ThreadPoolExecutor(
        max_workers=8, 
        thread_name_prefix="main_thread_pool"
        ) as worker_pool:
        futures = {
            worker_pool.submit(get_attachments, "random") \
                for _ in range(0, num_requests)
        }

    for ftre in futures:
        result = ftre.result()
        print(result)

    return None


# main ========================================================================
if __name__ == "__main__":
    main()
