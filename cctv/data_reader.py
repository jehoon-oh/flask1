import pandas as pd
import googlemaps
import json

class DataReader:
    def __init__(self):
        self._context = None
        self._fname = None

    @property
    def context(self) -> object: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> object: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    def new_file(self) -> str: return self._context + self._fname

    def csv_to_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        file = self.new_file()
        return pd.read_excel(file, encoding='UTF-8', header=header, usecols=usecols)

    def create_gmaps(self):
        # 구글지도 API 키는 반드시 지우고 깃허브 commit해야 함. 해킹당할 가능성 큼
        gmaps = googlemaps.Client(key='*****')

        # print(gmaps.geocode('서울중부경찰서', language='ko'))
        return gmaps

    def json_load(self):
        file = self.new_file()
        return json.load(open(file, encoding='utf-8'))
