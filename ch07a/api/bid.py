from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Bids
from repository.bids import BidsRepository
from models.request.bids import BidsReq
from db_config.sqlalchemy_connect import sess_db

from fastapi.security import HTTPBasicCredentials
from security.secure import http_basic

router = APIRouter()


@router.post("/bid/add")
def add_bid(
    req: BidsReq,
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess: Session = Depends(sess_db),
):
    bid_dict = req.dict(exclude_unset=True)
    repo: BidsRepository = BidsRepository(sess)
    bid = Bids(**bid_dict)
    result = repo.insert_bid(bid)
    if result is True:
        return bid
    else:
        return JSONResponse(
            content={"message": "create bid problem encountered"},
            status_code=500
        )


@router.patch("/bid/update")
def update_bid(
    id: int,
    req: BidsReq,
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess: Session = Depends(sess_db),
):
    bid_dict = req.dict(exclude_unset=True)
    repo: BidsRepository = BidsRepository(sess)
    result = repo.update_bid(id, bid_dict)
    if result:
        return JSONResponse(
            content={"message": "bid updated successfully"}, status_code=201
        )
    else:
        return JSONResponse(content={"message": "update bid error"},
                            status_code=500)


@router.delete("/bid/delete/{id}")
def delete_bid(
    id: int,
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess: Session = Depends(sess_db),
):
    repo: BidsRepository = BidsRepository(sess)
    result = repo.delete_bid(id)
    if result:
        return JSONResponse(
            content={"message": "auction updated successfully"},
            status_code=201
        )
    else:
        return JSONResponse(
            content={"message": "update auction error"}, status_code=500
        )


@router.get("/bid/all")
def list_all_bid(
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess: Session = Depends(sess_db),
):
    repo: BidsRepository = BidsRepository(sess)
    result = repo.get_all_bids()
    return result


@router.post("/bid/{id}")
def get_bid(
    id: int,
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess: Session = Depends(sess_db),
):
    repo: BidsRepository = BidsRepository(sess)
    result = repo.get_bid(id)
    return result
