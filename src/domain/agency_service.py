class AgencyService:
    
    def __init__(self, agency_repository=None):
        self.__agency_repository = agency_repository
    
    def find_by_id(self, agency_id):
        return self.__agency_repository.get_by_id(agency_id)
    
    def find_all(self):
        return self.__agency_repository.get_all()
    
    def create(self, agency):
        return self.__agency_repository.create(agency)
    
    def update(self, agency):
        return self.__agency_repository.update(agency)
    
    def delete(self, agency):
        return self.__agency_repository.delete(agency)