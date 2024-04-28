from json import load
from requests import get, post
from openpyxl import Workbook
from time import sleep

file = open('city.json')


search_item = [
    "DJ",]

loaded_file = load(file)


def search(
        city_id, page, searchTerm
):
    url = "https://gainr.in:443/api/tr/v1/filter-result"
    cookies = {"_ga_BBJ5R8BQVS": "GS1.1.1714289236.6.1.1714289699.0.0.0", "_ga": "GA1.1.1039194029.1714198007", "_gid": "GA1.2.954524776.1714198008", "_fbp": "fb.1.1714198012685.1524370137", "XSRF-TOKEN": "eyJpdiI6InJ0MUsrXC9BVDJzMHFQU2hEdFhCS0dRPT0iLCJ2YWx1ZSI6IjZyQ1JlQnBzcStmZ0ExMzc1VEp4WUZ3TTZoY3RhUkpVMjFGbkY0Z25kcEYxQlNVS3QxV1FJRkl1ZmZjS2FUdjQiLCJtYWMiOiJjOTJiOGQ2OTcyYWQxNTMxZjgzNWY5ZWVlNDAxOGVmODEyZDA0ZGFiZWQxMGIxYjBmMTNkZDA2YWU0ZDUzNWFmIn0%3D",
               "torbit_session": "eyJpdiI6InFVZVVwaWtROEczN2swazFMdEM5dFE9PSIsInZhbHVlIjoiV3I1QVZrZDVScU03U2MzbW8weEMrcUFIcWhtQnZ4TFM4bUVxRXdUR1lcL0xBY1FlQTFkZTZFZmdRQkRobTVXQ24iLCJtYWMiOiI0ZDg0MzViNGVlY2RlMWNiNzJjMzgyMTMzNWM3NzkxMzQzZjBjOGQ2ZDNmMjQwZWE3N2E5Zjk4Mzk3NjNjMjA4In0%3D", "_gat": "1"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Referer": "https://gainr.in/search/dj/NewDelhi", "Origin": "https://gainr.in", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2ZlNWNlMjY4ZjdhYTQyYWE4ZTlmMzdkOTM4ZGJkMmMzYzA5ZTA1ZTI1ZDc5YWVhZmI3OWUxNzMyMTNhN2Y2YzQ1ZDgxNWE3NjI0MmQ3ODkiLCJpYXQiOjE3MTQxOTkyNTAsIm5iZiI6MTcxNDE5OTI1MCwiZXhwIjoxNzQ1NzM1MjUwLCJzdWIiOiIyNDQ4MTUiLCJzY29wZXMiOltdfQ.EKPT6yRvJpsaq3b04ipalreZfIbo4AwurWJV_GbUcT41JrAXeewywCsOT3uVb26LlCbGQJWV8ITxajAjRJmnnpMsj_gD-QvTj4TqwDqdui3_ZTGML3TtJfNUJtLWz4hz8lDHIeSD2pYryDIAP2RXbmgFCE_muZ7JWYuAzBDsiZgarEonNyWn4AGjv8vTZZR6B5mhZ8ULO2LIN24BNWrvG_R9mv399GvxdUtuhgoLGr5eS9GJ2NIxb8BPsUYEdUkKAr9PnJvKItHlblO2wLDVu21-t-r-imxNZtohIkSA8j1LpDqfNd8SVw9OXSo41p1i0zoU77rofidLq24FVGbxABXsrXACA89NsHTCDZ1-FU7LAS60fWpBDqu07QpGZm6tUafBm4h28i2uKpnXNMYiE_7S6snNb-iKuilH1GfpDUfE303IyI0Gsvgr51ByVRgQU38LVK1y3H8MTx-dyr8KKHXseGiJa84MVCJB4bAmSP6SYgGCUjMEclugFvWtYUHxUE6bxaRWW2viqlLjFA8LAzGbPxvKWIB_kL8hZgvdlkPWO-5ab-cq9C9uer4NrCKJIEYAIpwx2FHHnvk8-ntVywcQVWvlRYQyFKBCFiyOqz5Zk1TQ-_NXZynUeow-yUIRVpKzYZV2i5J0QUhPRNbPDyHInP1rjTqSaxry90xxWs8", "Te": "trailers", "Connection": "close"}
    json = {"filter": {"city_id": city_id},
            "page": page, "searchTerm": searchTerm}

    data = post(
        url, headers=headers, cookies=cookies, json=json
    ).json()

    return data


def getContact(id):

    url = "https://gainr.in:443/api/tr/v1/view-contact"
    cookies = {"_ga_BBJ5R8BQVS": "GS1.1.1714289236.6.1.1714289805.0.0.0", "_ga": "GA1.1.1039194029.1714198007", "_gid": "GA1.2.954524776.1714198008", "_fbp": "fb.1.1714198012685.1524370137", "XSRF-TOKEN": "eyJpdiI6IlhHRkJoSnNuY0RaeWJINFl2eXhlU0E9PSIsInZhbHVlIjoiNDZGUjRcL2l1eEh2V1JUcTRjR2pYenhQM0xxY3JwcUdBTmswa0lVNUpOVnRzdDl1U3FUWUtzSHkyTGpuRktqbW8iLCJtYWMiOiJkZDZkOGI1YmE1MWJhNDE4OWZkYmRkNDNjMjg1Mzg2Njg0YTAzNTJlYzcyN2U1ZGMxNDUxZGUxMmNlZDVjYzM2In0%3D",
               "torbit_session": "eyJpdiI6IkNlZVh0QmZuc0FBdUxiY1N3WmdHWmc9PSIsInZhbHVlIjoiQXlRQUQya2FzODJGT3RRUjRESEZqMUZoUytwQVFCTnRNenQ1QjZpOHhwVGhxMlFVcEtlWmpON2Y0RTEyUmFDUiIsIm1hYyI6Ijg5OWNkOWJkYmVmZTc4YzE0NjA4OTAyNTllODQ2NTIyZjJjZjFhMmY4YmYyZjE4ZjFlNTIyNTA1MTdmZmJhMTkifQ%3D%3D", "_gat": "1"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/json", "Referer": "https://gainr.in/view/dj-headphones-headset-for-hourly-rent-Hathoj-Jaipur-0qaMjqXVlu", "Origin": "https://gainr.in", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2ZlNWNlMjY4ZjdhYTQyYWE4ZTlmMzdkOTM4ZGJkMmMzYzA5ZTA1ZTI1ZDc5YWVhZmI3OWUxNzMyMTNhN2Y2YzQ1ZDgxNWE3NjI0MmQ3ODkiLCJpYXQiOjE3MTQxOTkyNTAsIm5iZiI6MTcxNDE5OTI1MCwiZXhwIjoxNzQ1NzM1MjUwLCJzdWIiOiIyNDQ4MTUiLCJzY29wZXMiOltdfQ.EKPT6yRvJpsaq3b04ipalreZfIbo4AwurWJV_GbUcT41JrAXeewywCsOT3uVb26LlCbGQJWV8ITxajAjRJmnnpMsj_gD-QvTj4TqwDqdui3_ZTGML3TtJfNUJtLWz4hz8lDHIeSD2pYryDIAP2RXbmgFCE_muZ7JWYuAzBDsiZgarEonNyWn4AGjv8vTZZR6B5mhZ8ULO2LIN24BNWrvG_R9mv399GvxdUtuhgoLGr5eS9GJ2NIxb8BPsUYEdUkKAr9PnJvKItHlblO2wLDVu21-t-r-imxNZtohIkSA8j1LpDqfNd8SVw9OXSo41p1i0zoU77rofidLq24FVGbxABXsrXACA89NsHTCDZ1-FU7LAS60fWpBDqu07QpGZm6tUafBm4h28i2uKpnXNMYiE_7S6snNb-iKuilH1GfpDUfE303IyI0Gsvgr51ByVRgQU38LVK1y3H8MTx-dyr8KKHXseGiJa84MVCJB4bAmSP6SYgGCUjMEclugFvWtYUHxUE6bxaRWW2viqlLjFA8LAzGbPxvKWIB_kL8hZgvdlkPWO-5ab-cq9C9uer4NrCKJIEYAIpwx2FHHnvk8-ntVywcQVWvlRYQyFKBCFiyOqz5Zk1TQ-_NXZynUeow-yUIRVpKzYZV2i5J0QUhPRNbPDyHInP1rjTqSaxry90xxWs8", "Te": "trailers", "Connection": "close"}
    json = {"prosperId": str(id)}

    sleep(1)

    data = post(url, headers=headers, cookies=cookies, json=json).json()
    return data


for item in search_item:
    wb = Workbook()
    wa = wb.active

    try:

        id_list = []
        print(item)
        for _ in loaded_file:
            print("\t\t" + _["city_name"])
            wa.append(["", _["city_name"]])
            for page in range(1, 50):

                search_res = search(_["city_id"],  page, item)

                wa.append(["", _["city_name"]])

                if search_res["data"]:

                    for data in search_res["data"]:
                        id = data['user']['prosper_id']
                        if id not in id_list:
                            id_list.append(id)
                            user_details = getContact(id)
                        else:
                            continue
                        if user_details['data']:

                            print(id)

                            user_details_data = user_details['data']
                            name = user_details_data["name"]
                            title = data["title"]
                            description = data["description"]
                            phone = user_details_data["phone"]
                            email = user_details_data['email']
                            state = user_details_data["state"]
                            city = user_details_data['city']
                            rental_fee = data["rental_fee"]
                            rental_duration = data['rental_duration']
                            wa.append([
                                "", "",  name, title, description, phone, email, state, city, rental_fee, rental_duration
                            ])
                else:
                    break
    except:
        pass
    wb.save(f'{item}.xlsx')
