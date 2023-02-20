from typing import List

from fastapi import FastAPI, Query, Path, Body

from schemas import Book, Author, BookOut

app = FastAPI()


@app.post("/book",
          # response_model=Book,
          response_model=BookOut,
          # response_model_exclude_unset=True,
          response_model_exclude={"pages", "date"},  # передаем свойства, которые нужно исключить из ответа
          # response_model_include={"title", "writer", "duration"},  # передаем свойства, которые нужно показать в отвесе сервера
          )
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
def create_book(item: Book):
    # return {"item": item, "author": author, "quantity": quantity}
    # return {"item": item}
    # return item
    return BookOut(**item.dict(), id=3)


@app.post("/author")
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.get("/book")
def get_book(q: List[str] = Query(["test1", "test2"],
                                  min_length=2,
                                  max_length=10,
                                  description="Search book")):
    return q


@app.get("/book/{pk}")
def get_single_book(pk: int = Path(..., gt=1), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}
