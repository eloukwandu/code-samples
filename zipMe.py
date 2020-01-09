class ZipMe():

    def zip_me_now(self):
        firstNames = ["Elochukwu", "Ikenna", "Maduka", "Chinemerem"]
        lastNames = ["Ukwandu","Udodiri","Izuogu","Uche"]

        names = zip(firstNames, lastNames)

        for a, b in names:
            print(a,b)


    def sorting_min_max(self):
                stocks = {'GOOG': 99.23, 'YAHOO': 34.45, 'APPLE': 503.24, 'FB': 76.45}
        z = zip(stocks.values(), stocks.keys())
        mn = min(zip(stocks.values(), stocks.keys()))
        mx = max(zip(stocks.values(), stocks.keys()))
        sr = sorted(zip(stocks.values(), stocks.keys()))
        print(mn, "\n", mx, "\n", sr)


r = ZipMe()
r.zip_me_now()
print()
r.sorting_min_max()
