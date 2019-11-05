import requests
from unittest import TestCase
from test_functions import compare_get_request, compare_post_request

class TestFeatures(TestCase):

    def test_advancedSearch(self):
        compare_get_request("/advancedSearch")

    def test_createCollection(self):
        compare_get_request("/createCollection")

    def test_resetPassword(self):
        compare_get_request("/resetPassword")

    def test_browse(self):
        compare_get_request("/browse")

    def test_sparql(self):
        compare_get_request("/sparql", headers = {"Accept": "text/html"})

    def test_searchQuery(self):
        compare_get_request("/search/:query?", route_parameters = ["I0462"])

    def test_searchCount(self):
        compare_get_request("/searchCount/:query?", route_parameters = ["I0462"])        

    def test_advancedSearchQuery(self):
        compare_get_request("/advancedSearch/:query?", route_parameters = ["I0462"])        

    def test_autocompleteQuery(self):
        compare_get_request("/autocomplete/:query", route_parameters = ["I0462"])

    def test_createCollectionQuery(self):
        compare_get_request("/createCollection/:query?", route_parameters = ["test"])

    def test_rootCollections(self):
        compare_get_request("/rootCollections")

    def test_typeCount(self):
        compare_get_request("/:type/count", route_parameters = ["Component"])
