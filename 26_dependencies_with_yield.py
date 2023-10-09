# Dependencies with yield


# fake database session manager
class DBSession:

    def close(self):
        pass


async def get_db():
    # Only the code prior to and including the yield statement is executed before sending a response:
    db = DBSession()
    try:
        # The yielded value is what is injected into path operations and other dependencies:
        yield db
    # The code following the yield statement is executed after the response has been delivered:
    finally:
        db.close()
