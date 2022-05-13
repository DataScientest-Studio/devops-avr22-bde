from fastapi import FastAPI

api = FastAPI(title="Mon API pour les AVR22 BDE")


# GET {url_de_l_api}/
@api.get("/")
def get_index():
    return {
        "hello": "world"
    }


@api.delete("/mon_delete", tags=["fonctions exemples"],
            responses={
                200: {
                    "description": "Tout va bien !!! :) :) "
                }
})
def ma_fonction():
    """Ceci est un exemple de DELETE"""
    return {
        "method": "delete"
    }


@api.post("/mon_post")
def post_mon_post():
    return {
        "method": "post"
    }