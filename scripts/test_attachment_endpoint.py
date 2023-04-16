r""" scripts.test_attachment_endpoint module """


# importing standard modules ==================================================
from typing import List, Dict, Any
from concurrent.futures import (
    ThreadPoolExecutor, 
    as_completed
)


# importing third-party modules ===============================================
from requests import (
    Session,
    Response
)


# method definitions ==========================================================
def get_attachments(session: Session, ucid: str) -> List[Dict[str, Any]]:
    url: str = "http://localhost:8000/api/v1/attachment/list"
    __params: Dict[str, str] = {"ucid": ucid}
   
    response: Response = session.get(url, params=__params)
    
    data: Dict[str, Any] = response.json()
    num_items: int = int(data.get("items"))
    attachments: List[Dict[str, Any]] = data.get("attachments")
    assert len(attachments) == num_items
    return attachments


def main() -> None:

    num_requests: int = 100
    sample_ucid: str = "US-9145048-B2"

    futures = list()
    with ThreadPoolExecutor(
        max_workers=8, 
        thread_name_prefix="main_thread_pool"
        ) as worker_pool:

        with Session() as session:
            futures = {
                worker_pool.submit(get_attachments, session, sample_ucid)
                for _ in range(0, num_requests)
            }

    for ftre in as_completed(futures):
        result = ftre.result()
        print(result)

    # with Session() as session:
    #     for _ in range(0, num_requests):
    #         __f = get_attachments(session, sample_ucid)
    #         print( __f )

    return None


# main ========================================================================
if __name__ == "__main__":
    main()
