from json import dump
cities =  [
      {
        "id": 1309,
        "city": "Achalpur",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1,
        "city": "Adilabad",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1353,
        "city": "Adoni",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1133,
        "city": "Adoor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1114,
        "city": "Afzalpur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 2,
        "city": "Agar Malwa",
        "state_id": 13,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 3,
        "city": "Agartala",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 876,
        "city": "Agasteeswaram",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 4,
        "city": "Agra",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 5,
        "city": "Ahmed Nagar",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 6,
        "city": "Ahmedabad",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 7,
        "city": "Aizawl",
        "state_id": 17,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 8,
        "city": "Ajmer",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1033,
        "city": "Akathiyoor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1079,
        "city": "Akhnoor",
        "state_id": 35,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 9,
        "city": "Akola",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1199,
        "city": "Aland",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 880,
        "city": "Alangudi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 883,
        "city": "Alangulam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 10,
        "city": "Alappuzha",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 11,
        "city": "Aligarh",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1323,
        "city": "Alipurduar",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 12,
        "city": "Alirajpur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 13,
        "city": "Allahabad",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 14,
        "city": "Almora",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 15,
        "city": "Alwar",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 16,
        "city": "Ambala",
        "state_id": 8,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1385,
        "city": "Ambarnath",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1425,
        "city": "Ambattur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 17,
        "city": "Ambedkar Nagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1313,
        "city": "Ambikapur",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 744,
        "city": "Ambur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 18,
        "city": "Amethi",
        "state_id": 26,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1037,
        "city": "Amini",
        "state_id": 34,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 19,
        "city": "Amlapuram",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 20,
        "city": "Amravati",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 21,
        "city": "Amreli",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 22,
        "city": "Amritsar",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 23,
        "city": "Amroha",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1466,
        "city": "Anakapalle",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 24,
        "city": "Anand",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 25,
        "city": "Anantapur",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 26,
        "city": "Ananthnag",
        "state_id": 35,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1086,
        "city": "Ancharakandy",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 884,
        "city": "Andipatti",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1047,
        "city": "Andrott",
        "state_id": 34,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1202,
        "city": "Anekal",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 27,
        "city": "Angul",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1083,
        "city": "Anjaw",
        "state_id": 2,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1090,
        "city": "Ankola",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1125,
        "city": "Annigeri",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 875,
        "city": "Anthiyur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1124,
        "city": "Anthoor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 28,
        "city": "Anuppur",
        "state_id": 13,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 745,
        "city": "Arakkonam",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 872,
        "city": "Arani",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 881,
        "city": "Aranthangi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 29,
        "city": "Araria",
        "state_id": 4,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 877,
        "city": "Aravakurichi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 30,
        "city": "Aravalli",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 746,
        "city": "Arcot",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 31,
        "city": "Ariyalur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1256,
        "city": "Armur",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1065,
        "city": "Arookutty",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1167,
        "city": "Aroor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1387,
        "city": "Arrah",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 32,
        "city": "Arsikere",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 747,
        "city": "Aruppukkottai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 33,
        "city": "Arwal",
        "state_id": 4,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1450,
        "city": "Asansol",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 34,
        "city": "Ashok Nagar",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1472,
        "city": "Atal Nagar",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 35,
        "city": "Athani",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1168,
        "city": "Attingal",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 874,
        "city": "Attur",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 36,
        "city": "Auraiya",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 37,
        "city": "Aurangabad",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1297,
        "city": "Aurangabad",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1410,
        "city": "Avadi",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 38,
        "city": "Avanigadda",
        "state_id": 1,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 886,
        "city": "Avinashi",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1050,
        "city": "Avinissery",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 39,
        "city": "Azamgarh",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1147,
        "city": "Badami",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 40,
        "city": "Bagalkot",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1113,
        "city": "Bagepalli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 41,
        "city": "Bageshwar",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 42,
        "city": "Bagpat",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 43,
        "city": "Bahraich",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 44,
        "city": "Bailhongal",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 45,
        "city": "Baksa",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 46,
        "city": "Balaghat",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 47,
        "city": "Balangir",
        "state_id": 19,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 48,
        "city": "Balasore",
        "state_id": 19,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 49,
        "city": "Baleswar",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 51,
        "city": "Ballia",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1310,
        "city": "Bally",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 52,
        "city": "Balod",
        "state_id": 5,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 54,
        "city": "Balrampur",
        "state_id": 26,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 55,
        "city": "Banaskantha",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 56,
        "city": "Banda",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 57,
        "city": "Bandipur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1175,
        "city": "Bandipura",
        "state_id": 35,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1207,
        "city": "Bangarapet",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 58,
        "city": "Banka",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1092,
        "city": "Bankapura",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 59,
        "city": "Bankura",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1087,
        "city": "Bannur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 60,
        "city": "Banswara",
        "state_id": 21,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1191,
        "city": "Bantval",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 61,
        "city": "Bapatla",
        "state_id": 1,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 62,
        "city": "Barabanki",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 63,
        "city": "Baramulla",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 64,
        "city": "Baran",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1381,
        "city": "Baranagar",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1390,
        "city": "Barasat",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 65,
        "city": "Bardhaman",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 66,
        "city": "Bareilly",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 67,
        "city": "Bargarh",
        "state_id": 19,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 68,
        "city": "Barmer",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 69,
        "city": "Barnala",
        "state_id": 20,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 70,
        "city": "Barpeta",
        "state_id": 3,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1318,
        "city": "Barshi",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 71,
        "city": "Barwani",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1270,
        "city": "Basavakalyan",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1158,
        "city": "Basavana Bagevadi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 72,
        "city": "Bastar",
        "state_id": 5,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 73,
        "city": "Basti",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 74,
        "city": "Bathinda",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1335,
        "city": "Beawar",
        "state_id": 21,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 75,
        "city": "Beed",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 76,
        "city": "Begusarai",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 78,
        "city": "Belgaum",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1240,
        "city": "Bellampalle",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 79,
        "city": "Bellary",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1091,
        "city": "Belur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 80,
        "city": "Bemetara",
        "state_id": 5,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 81,
        "city": "Bengaluru",
        "state_id": 11,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 1360,
        "city": "Berhampore",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1412,
        "city": "Berhampur",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1325,
        "city": "Bettiah",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 82,
        "city": "Betul",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 590,
        "city": "Bhadohi",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 83,
        "city": "Bhadrachalam",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 84,
        "city": "Bhadrak",
        "state_id": 19,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1252,
        "city": "Bhadravati",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 85,
        "city": "Bhagalpur",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1192,
        "city": "Bhalki",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1336,
        "city": "Bhalswa Jahangir Pur",
        "state_id": 32,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 86,
        "city": "Bhandara",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 87,
        "city": "Bharatpur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 88,
        "city": "Bharuch",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1154,
        "city": "Bhatkal",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1418,
        "city": "Bhatpara",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 748,
        "city": "Bhavani",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 89,
        "city": "Bhavnagar",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1448,
        "city": "Bhilai",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 90,
        "city": "Bhilwara",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1028,
        "city": "Bhimavaram",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 91,
        "city": "Bhind",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1413,
        "city": "Bhivandi Nizampur",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1395,
        "city": "Bhiwadi",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 92,
        "city": "Bhiwani",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 93,
        "city": "Bhojpur",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 94,
        "city": "Bhongir",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 95,
        "city": "Bhopal",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1445,
        "city": "Bhubaneswar",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1374,
        "city": "Bhuj",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 96,
        "city": "Bhupalpalli",
        "state_id": 24,
        "price": 25,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 97,
        "city": "Bhusawal",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 887,
        "city": "Bhuvanagiri",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 98,
        "city": "Bidar",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1372,
        "city": "Bidhannagar",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1397,
        "city": "Bihar Sharif",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1096,
        "city": "Bijbiara",
        "state_id": 35,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 100,
        "city": "Bijnor",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 101,
        "city": "Bikaner",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 102,
        "city": "Bilaspur",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1417,
        "city": "Bilaspur",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 103,
        "city": "Birbhum",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1095,
        "city": "Birur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1380,
        "city": "Bishnupur",
        "state_id": 15,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 104,
        "city": "Bishnupur",
        "state_id": 28,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1280,
        "city": "Bodhan",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 890,
        "city": "Bodinayakanur",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 105,
        "city": "Bokaro",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 106,
        "city": "Bongaigaon",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 107,
        "city": "Botab",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 108,
        "city": "Boudh",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 109,
        "city": "Budaun",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 110,
        "city": "Budgam",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 111,
        "city": "Bulandshahr",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 112,
        "city": "Buldhana",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 113,
        "city": "Bundi",
        "state_id": 21,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 114,
        "city": "Burhanpur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 115,
        "city": "Buxar",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1142,
        "city": "Byadgi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 116,
        "city": "Cachar",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1022,
        "city": "Calangute",
        "state_id": 6,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 117,
        "city": "Central Delhi",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1058,
        "city": "Chala",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1221,
        "city": "Chalakudy",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1239,
        "city": "Challakere",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 118,
        "city": "Chamarajanagar",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 119,
        "city": "Chamba",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1436,
        "city": "Chamba",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 120,
        "city": "Chamoli",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 121,
        "city": "Champawat",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 122,
        "city": "Champhai",
        "state_id": 17,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 123,
        "city": "Chandauli",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 124,
        "city": "Chandel",
        "state_id": 15,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 125,
        "city": "Chandigarh",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 126,
        "city": "Chandrapur",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1228,
        "city": "Changanassery",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 127,
        "city": "Changlang",
        "state_id": 2,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1084,
        "city": "Channagiri",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1276,
        "city": "Channapatna",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1194,
        "city": "Channarayapatna",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1363,
        "city": "Chapra",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1431,
        "city": "Charkhi Dadri",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 128,
        "city": "Chatra",
        "state_id": 10,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1186,
        "city": "Chavakkad",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1074,
        "city": "Chelora",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1122,
        "city": "Chendamangalam",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 749,
        "city": "Chengalpattu",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 892,
        "city": "Chengam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1106,
        "city": "Chengannur",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 129,
        "city": "Chennai",
        "state_id": 23,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 893,
        "city": "Cheranmahadevi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1188,
        "city": "Cherpulassery",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1210,
        "city": "Cherthala",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1109,
        "city": "Cheruthazham",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1064,
        "city": "Chevvoor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 891,
        "city": "Cheyyur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 130,
        "city": "Chhatarpur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 131,
        "city": "Chhindwara",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 132,
        "city": "Chhota Udaipur",
        "state_id": 7,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 134,
        "city": "Chikkaballapur",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 135,
        "city": "Chikkamagaluru",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1115,
        "city": "Chiknayakanhalli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1189,
        "city": "Chikodi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1296,
        "city": "Chilakaluripeta",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1082,
        "city": "Chincholi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 751,
        "city": "Chinnasalem",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1394,
        "city": "Chinsurah",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1279,
        "city": "Chintamani",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1300,
        "city": "Chirmiri",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1149,
        "city": "Chitapur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1105,
        "city": "Chitgoppa",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 136,
        "city": "Chitradurga",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 137,
        "city": "Chitrakoot",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 138,
        "city": "Chittoor",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 139,
        "city": "Chittorgarh",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1264,
        "city": "Chittur Thathamangalam",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1152,
        "city": "Chockli",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1046,
        "city": "Chuglamsar",
        "state_id": 33,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 140,
        "city": "Churachandpur",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 141,
        "city": "Churu",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 142,
        "city": "Coimbatore",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 143,
        "city": "Cooch Behar",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 753,
        "city": "Coonoor",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1023,
        "city": "Coorg",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 144,
        "city": "Cuddalore",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 145,
        "city": "Cuttack",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 146,
        "city": "Dadra Nagar Haveli",
        "state_id": 31,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 147,
        "city": "Dahod",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1344,
        "city": "Dakshin Dinajpur",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 148,
        "city": "Dakshina Kannada",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 149,
        "city": "Daman",
        "state_id": 31,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 150,
        "city": "Damoh",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1349,
        "city": "Danapur",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1229,
        "city": "Dandeli",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 151,
        "city": "Dangs",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 152,
        "city": "Dantewada",
        "state_id": 5,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 153,
        "city": "Darbhanga",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 154,
        "city": "Darjeeling",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 155,
        "city": "Darrang",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 156,
        "city": "Datia",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 157,
        "city": "Dausa",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 158,
        "city": "Davangere",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 159,
        "city": "Debagarh",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1307,
        "city": "Deesa",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 160,
        "city": "Dehradun",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 894,
        "city": "Denkanikottai",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 161,
        "city": "Deoghar",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 162,
        "city": "Deoria",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1132,
        "city": "Devadurga",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 895,
        "city": "Devakottai",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1119,
        "city": "Devanahalli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 163,
        "city": "Devbhoomi Dwerka",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 164,
        "city": "Dewas",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 165,
        "city": "Dhalai",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 166,
        "city": "Dhamtari",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 167,
        "city": "Dhanbad",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 168,
        "city": "Dhar",
        "state_id": 13,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 896,
        "city": "Dharapuram",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 169,
        "city": "Dharmanagar",
        "state_id": 25,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 170,
        "city": "Dharmapuri",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 171,
        "city": "Dharmavaram",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 172,
        "city": "Dharwad",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1326,
        "city": "Dhaulpur",
        "state_id": 21,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 173,
        "city": "Dhemaji",
        "state_id": 3,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 174,
        "city": "Dhenkanal",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 175,
        "city": "Dholpur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 176,
        "city": "Dhubri",
        "state_id": 3,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 177,
        "city": "Dhule",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 178,
        "city": "Dibang Valley",
        "state_id": 1,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 179,
        "city": "Dibrugarh",
        "state_id": 3,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 180,
        "city": "Dima Hasao",
        "state_id": 3,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 181,
        "city": "Dimapur",
        "state_id": 18,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 182,
        "city": "Dindigul",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 183,
        "city": "Dindori",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 184,
        "city": "Diu",
        "state_id": 31,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 185,
        "city": "Doda",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1291,
        "city": "Doddaballapur",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1457,
        "city": "Dudhrej",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 186,
        "city": "Dumka",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 187,
        "city": "Dungarpur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 188,
        "city": "Durg",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1467,
        "city": "Durgapur",
        "state_id": 14,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1438,
        "city": "Durgapur",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1097,
        "city": "DuruVerinag",
        "state_id": 35,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1474,
        "city": "Dwarka",
        "state_id": 7,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 189,
        "city": "East Champaran",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 190,
        "city": "East Delhi",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 191,
        "city": "East Garo Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 192,
        "city": "East Godavari",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 193,
        "city": "East Jaintia Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 194,
        "city": "East Kameng",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 195,
        "city": "East Khasi Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 196,
        "city": "East Midnapore",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 197,
        "city": "East Siang",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 198,
        "city": "East Sikkim",
        "state_id": 22,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 199,
        "city": "East Singhbhum",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1373,
        "city": "Eluru",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 898,
        "city": "Eral",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1165,
        "city": "Erattupetta",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 200,
        "city": "Ernakulam",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 201,
        "city": "Erode",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 202,
        "city": "Etah",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 203,
        "city": "Etawah",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 899,
        "city": "Ettayapuram",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1225,
        "city": "Ettumanoor",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 204,
        "city": "Faizabad",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 205,
        "city": "Faridabad",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 206,
        "city": "Faridkot",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 207,
        "city": "Farrukhabad",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 208,
        "city": "Fatehabad",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1449,
        "city": "Fatehabad",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 209,
        "city": "Fatehgarh Sahib",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 210,
        "city": "Fatehpur",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 211,
        "city": "Fazilka",
        "state_id": 20,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1237,
        "city": "Feroke",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 212,
        "city": "Ferozepur",
        "state_id": 20,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 213,
        "city": "Firozabad",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 215,
        "city": "Gadag",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 216,
        "city": "Gadchiroli",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 217,
        "city": "Gadwal",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 218,
        "city": "Gajapati",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1156,
        "city": "Gajendragarh",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 901,
        "city": "Gandarvakottai",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 219,
        "city": "Ganderbal",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1382,
        "city": "Gandhidham",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 220,
        "city": "Gandhinagar",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1302,
        "city": "Gangawati",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 221,
        "city": "Ganjam",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 222,
        "city": "Garhwa",
        "state_id": 10,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 223,
        "city": "Gariaband",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1182,
        "city": "Gauribidanur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 224,
        "city": "Gautam Buddha Nagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 225,
        "city": "Gaya",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 226,
        "city": "Ghaziabad",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 227,
        "city": "Ghazipur",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 903,
        "city": "Gingee",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1473,
        "city": "Gir Somnath",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 228,
        "city": "Giridih",
        "state_id": 10,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 229,
        "city": "Girmnath",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1471,
        "city": "Goa",
        "state_id": 6,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 230,
        "city": "Goalpara",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 900,
        "city": "Gobichettipalayam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 231,
        "city": "Godda",
        "state_id": 10,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1330,
        "city": "Godhara",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1281,
        "city": "Gokak",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 232,
        "city": "Golaghat",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 233,
        "city": "Gomati",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 234,
        "city": "Gonda",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1348,
        "city": "Gondal",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 235,
        "city": "Gondia",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 236,
        "city": "Gopalganj",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1038,
        "city": "Gopalpur",
        "state_id": 28,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 237,
        "city": "Gorakhpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 758,
        "city": "Gudalur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1327,
        "city": "Gudivada",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 759,
        "city": "Gudiyatham",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 238,
        "city": "Gulbarga",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1160,
        "city": "Guledgudda",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 239,
        "city": "Gumla",
        "state_id": 10,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 904,
        "city": "Gummidipoondi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 240,
        "city": "Guna",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1121,
        "city": "Gundlupet",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1322,
        "city": "Guntakal",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 241,
        "city": "Guntur",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 242,
        "city": "Gurdaspur",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 243,
        "city": "Gurgaon",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1077,
        "city": "Gurmatkal",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1328,
        "city": "Guruvayur",
        "state_id": 12,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1018,
        "city": "Guwahati",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 244,
        "city": "Gwalior",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 245,
        "city": "Hailakandi",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1332,
        "city": "Hajipur",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1362,
        "city": "Haldia",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1424,
        "city": "Hamirpur",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 246,
        "city": "Hamirpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 247,
        "city": "Hanagodu",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 248,
        "city": "Hanamkonda",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1123,
        "city": "Hangal",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 249,
        "city": "Hanumangarh",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 250,
        "city": "Hapur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1214,
        "city": "Harapanahalli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 251,
        "city": "Harda",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 252,
        "city": "Hardoi",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 253,
        "city": "Haridwar",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1286,
        "city": "Harihar",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1148,
        "city": "Haripad",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 254,
        "city": "Hassan",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 255,
        "city": "Hathras",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1062,
        "city": "Hatti",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 256,
        "city": "Haveri",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 257,
        "city": "Hazaribagh",
        "state_id": 10,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1166,
        "city": "Hebbagodi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 258,
        "city": "Hindupur",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1298,
        "city": "Hinganghat",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 259,
        "city": "Hingoli",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1241,
        "city": "Hiriyur",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 260,
        "city": "Hisar",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1140,
        "city": "Hole Narsipur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1287,
        "city": "Homnabad",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 261,
        "city": "Hooghly",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1118,
        "city": "Hoovina Hadagalli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1027,
        "city": "Hosakote",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1126,
        "city": "Hosdurga",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 263,
        "city": "Hoshiarpur",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1364,
        "city": "Hospet",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 760,
        "city": "Hosur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 264,
        "city": "Howrah",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 265,
        "city": "Hubballi",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1102,
        "city": "Hukeri",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1081,
        "city": "Hungund",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 266,
        "city": "Hunsur",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 267,
        "city": "Hyderabad",
        "state_id": 24,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 1393,
        "city": "Ichalkaranji",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 268,
        "city": "Idukki",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1250,
        "city": "Ilkal",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 269,
        "city": "Imphal",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 270,
        "city": "Imphal East",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 271,
        "city": "Imphal West",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 272,
        "city": "Indore",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1251,
        "city": "Irinjalakuda",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1193,
        "city": "Iritty",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1468,
        "city": "Islampur",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1469,
        "city": "Islampur",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1312,
        "city": "Itarsi",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 273,
        "city": "Jabalpur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 274,
        "city": "Jagatsinghapur",
        "state_id": 19,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 275,
        "city": "Jagdalpur",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 276,
        "city": "Jagtial",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 277,
        "city": "Jaintia Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 278,
        "city": "Jaipur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 279,
        "city": "Jaisalmer",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 280,
        "city": "Jajpur",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 281,
        "city": "Jalandhar",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 282,
        "city": "Jalaun",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 283,
        "city": "Jalgaon",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 284,
        "city": "Jalna",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 285,
        "city": "Jalor",
        "state_id": 21,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 286,
        "city": "Jalpaiguri",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 287,
        "city": "Jamkhandi",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 288,
        "city": "Jammu",
        "state_id": 35,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 289,
        "city": "Jamnagar",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1453,
        "city": "Jamshedpur",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 290,
        "city": "Jamtara",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 291,
        "city": "Jamui",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 292,
        "city": "Jangaon",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 293,
        "city": "Janjgirchampa",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 294,
        "city": "Jaspur",
        "state_id": 27,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 295,
        "city": "Jaunpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 297,
        "city": "Jehanabad",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1317,
        "city": "Jetpur",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1107,
        "city": "Jevargi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 298,
        "city": "Jhabua",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 299,
        "city": "Jhajjar",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 300,
        "city": "Jhalawar",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 301,
        "city": "Jhansi",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 302,
        "city": "Jharsuguda",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 303,
        "city": "Jhujhunu",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 304,
        "city": "Jind",
        "state_id": 8,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 305,
        "city": "Jiribam",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 306,
        "city": "Jodhpur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 308,
        "city": "Jorhat",
        "state_id": 3,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 309,
        "city": "Junagadh",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 311,
        "city": "Kachchh",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 312,
        "city": "Kadapa",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1034,
        "city": "Kadmat",
        "state_id": 34,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1162,
        "city": "Kadur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1246,
        "city": "Kagaznagar",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 313,
        "city": "Kaimur Bhabua",
        "state_id": 4,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 314,
        "city": "Kaithal",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1155,
        "city": "Kakching",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1030,
        "city": "Kakinada",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 316,
        "city": "Kalahandi",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1271,
        "city": "Kalamassery",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 317,
        "city": "Kalghatgi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 318,
        "city": "Kalimpong",
        "state_id": 28,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 910,
        "city": "Kalkulam",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1120,
        "city": "Kalliasseri",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1032,
        "city": "Kalpeni",
        "state_id": 34,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1151,
        "city": "Kalpetta",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1452,
        "city": "Kalyan Dombivli",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 319,
        "city": "Kamareddy",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1406,
        "city": "Kamarhati",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1209,
        "city": "Kamjong",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1187,
        "city": "Kampli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 320,
        "city": "Kamrup",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1236,
        "city": "Kanakapura",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 321,
        "city": "Kanchipuram",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 918,
        "city": "Kandachipuram",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 322,
        "city": "Kandhamal",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1465,
        "city": "Kandhukur",
        "state_id": 1,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 927,
        "city": "Kangayam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1409,
        "city": "Kangpokpi",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 323,
        "city": "Kangra",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1324,
        "city": "Kanhangad",
        "state_id": 12,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1056,
        "city": "Kanhirode",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1089,
        "city": "Kanjikkuzhi",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 324,
        "city": "Kanker",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 325,
        "city": "Kannauj",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 326,
        "city": "Kannur",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1459,
        "city": "Kanpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 327,
        "city": "Kanpur Dehat",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 328,
        "city": "Kanpur Nagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 329,
        "city": "Kanshiram Nagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 330,
        "city": "Kanyakumari",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 331,
        "city": "Kapurthala",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 332,
        "city": "Karaikal",
        "state_id": 36,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 762,
        "city": "Karaikudi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 932,
        "city": "Karambakudi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 333,
        "city": "Karauli",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1463,
        "city": "Karawal Nagar",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 334,
        "city": "Karbi Anglong",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 335,
        "city": "Kargil",
        "state_id": 33,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 916,
        "city": "Kariapatti",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 337,
        "city": "Karimganj",
        "state_id": 3,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1398,
        "city": "Karimnagar",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1108,
        "city": "Karkala",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 338,
        "city": "Karnal",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1218,
        "city": "Karunagappalli",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 763,
        "city": "Karungal",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 339,
        "city": "Karur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1338,
        "city": "Karwar",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 340,
        "city": "Kasaragod",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1295,
        "city": "Kasganj",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 341,
        "city": "Kathua",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 342,
        "city": "Katihar",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 343,
        "city": "Katni",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 917,
        "city": "Katpadi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1200,
        "city": "Kattappana",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 906,
        "city": "Kattumannarkoil",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 344,
        "city": "Kaushambi",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1048,
        "city": "Kavaratti",
        "state_id": 34,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 345,
        "city": "Kawardha",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1265,
        "city": "Kayamkulam",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 913,
        "city": "Keelakarai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 346,
        "city": "Kendrapara",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 347,
        "city": "Kendujhar",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 348,
        "city": "Khagaria",
        "state_id": 4,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 349,
        "city": "Khammam",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1233,
        "city": "Khanapuram Haveli",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 350,
        "city": "Khandwa",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1400,
        "city": "Kharagpur",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1470,
        "city": "Kharagpur",
        "state_id": 4,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 351,
        "city": "Khargone",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 352,
        "city": "Kheda",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 353,
        "city": "Kheri",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1355,
        "city": "Khora",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 354,
        "city": "Khordha",
        "state_id": 19,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 355,
        "city": "Khowai",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 356,
        "city": "Khunti",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 357,
        "city": "Kinnaur",
        "state_id": 9,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 358,
        "city": "Kiphire",
        "state_id": 18,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1392,
        "city": "Kirari Suleman Nagar",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 359,
        "city": "Kishanganj",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1337,
        "city": "Kishangarh",
        "state_id": 21,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 360,
        "city": "Kochi",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 361,
        "city": "Kodagu",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 908,
        "city": "Kodaikanal",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 362,
        "city": "Koderma",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1292,
        "city": "Kodungallur",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1222,
        "city": "Koduvally",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 363,
        "city": "Kohima",
        "state_id": 18,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 364,
        "city": "Kokrajhar",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 365,
        "city": "Kolar",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 366,
        "city": "Kolasib",
        "state_id": 3,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1284,
        "city": "Kolasib",
        "state_id": 17,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 933,
        "city": "Kolathur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 367,
        "city": "Kolhapur",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 368,
        "city": "Kolkata",
        "state_id": 28,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 369,
        "city": "Kollam",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 765,
        "city": "Kollankodu",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 370,
        "city": "Kollegal",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 371,
        "city": "Kondagaon",
        "state_id": 5,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1248,
        "city": "Kondotty",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 930,
        "city": "Koothanallur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1069,
        "city": "Koothattukulam",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 372,
        "city": "Koppal",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 373,
        "city": "Koraput",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1262,
        "city": "Koratla",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1067,
        "city": "Koratty",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 374,
        "city": "Korba",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 375,
        "city": "Koriya",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 376,
        "city": "Kota",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1460,
        "city": "Kota",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1477,
        "city": "Kothagiri",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 377,
        "city": "Kothagudem",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1176,
        "city": "Kothamangalam",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1220,
        "city": "Kottakkal",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1143,
        "city": "Kottarakara",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 379,
        "city": "Kottayam",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 922,
        "city": "Kovilpatti",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 380,
        "city": "Kovvur",
        "state_id": 1,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1275,
        "city": "Koyilandy",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 381,
        "city": "Kozhikode",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 382,
        "city": "Krishna",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 383,
        "city": "Krishnagiri",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1169,
        "city": "Krishnarajanagara",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1110,
        "city": "Krishnarajpet",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 912,
        "city": "Krishnarayapuram",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1098,
        "city": "Kudchi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1085,
        "city": "Kudligi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 384,
        "city": "Kulgam",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 911,
        "city": "Kulithalai",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 385,
        "city": "Kullu",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1403,
        "city": "Kulti",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 923,
        "city": "Kumarapalayam",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 766,
        "city": "Kumbakonam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1174,
        "city": "Kumta",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1145,
        "city": "Kundapura",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 925,
        "city": "Kundrathur",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1163,
        "city": "Kunigal",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1227,
        "city": "Kunnamkulam",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 387,
        "city": "Kupwara",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 907,
        "city": "Kurinjipadi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 388,
        "city": "Kurnool",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 389,
        "city": "Kurukshetra",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 390,
        "city": "Kurung Kumey",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 391,
        "city": "Kushinagar",
        "state_id": 26,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1101,
        "city": "Kushtagi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1157,
        "city": "Kuthuparamba",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1389,
        "city": "Ladakh",
        "state_id": 33,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 392,
        "city": "Lahauland Spiti",
        "state_id": 9,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 393,
        "city": "Lakhimpur",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 394,
        "city": "Lakhisarai",
        "state_id": 4,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 395,
        "city": "Lakshadweep",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 767,
        "city": "Lalgudi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 396,
        "city": "Lalitpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 397,
        "city": "Latehar",
        "state_id": 10,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 398,
        "city": "Latur",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 399,
        "city": "Lawngtlai",
        "state_id": 17,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 400,
        "city": "Leh",
        "state_id": 35,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1146,
        "city": "Leh",
        "state_id": 33,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 401,
        "city": "Lohardaga",
        "state_id": 10,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 402,
        "city": "Lohit",
        "state_id": 2,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 403,
        "city": "Longleng",
        "state_id": 18,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1434,
        "city": "Loni",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 404,
        "city": "Lower Dibang Valley",
        "state_id": 2,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 405,
        "city": "Lower Subansiri",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 406,
        "city": "Lucknow",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 407,
        "city": "Ludhiana",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 408,
        "city": "Lunglei",
        "state_id": 17,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 409,
        "city": "Machilipatnam",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 410,
        "city": "Madanapalle",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 944,
        "city": "Madathukulam",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1131,
        "city": "Maddur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 411,
        "city": "Madhepura",
        "state_id": 4,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 412,
        "city": "Madhubani",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1136,
        "city": "Madhugiri",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1357,
        "city": "Madhyamgram",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 413,
        "city": "Madikeri",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 414,
        "city": "Madurai",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1141,
        "city": "Magadi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1478,
        "city": "Mahabalipuram",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 415,
        "city": "Mahabubabad",
        "state_id": 24,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 416,
        "city": "Mahabubnagar",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1172,
        "city": "Mahalingpur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 418,
        "city": "Maharajganj",
        "state_id": 4,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 419,
        "city": "Mahasamund",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 420,
        "city": "Mahe",
        "state_id": 36,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 421,
        "city": "Mahendragarh",
        "state_id": 8,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 422,
        "city": "Mahesana",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1423,
        "city": "Maheshtala",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 423,
        "city": "Mahisagar",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 424,
        "city": "Mahoba",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 425,
        "city": "Mainpuri",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 426,
        "city": "Makdi",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 427,
        "city": "Malappuram",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1180,
        "city": "Malavalli",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 428,
        "city": "Malda",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 429,
        "city": "Malegaon",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 430,
        "city": "Malkangiri",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1190,
        "city": "Malur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 431,
        "city": "Mamit",
        "state_id": 17,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 943,
        "city": "Manachanallur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 939,
        "city": "Manamadurai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 941,
        "city": "Manamelkudi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1219,
        "city": "Mananthavady",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 952,
        "city": "Manapparai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 432,
        "city": "Mancherial",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1231,
        "city": "Mandamarri",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 433,
        "city": "Mandi",
        "state_id": 9,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 434,
        "city": "Mandla",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 435,
        "city": "Mandsaur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 436,
        "city": "Mandya",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1305,
        "city": "Mangalagiri",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1021,
        "city": "Mangalore",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1376,
        "city": "Mango",
        "state_id": 10,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1293,
        "city": "Manjeri",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1043,
        "city": "Manjeshwar",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 942,
        "city": "Mannargudi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1153,
        "city": "Mannarkkad",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 437,
        "city": "Mansa",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 940,
        "city": "Manur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1213,
        "city": "Manvi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1206,
        "city": "Maradu",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 439,
        "city": "Mathura",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1203,
        "city": "Mattannur",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 440,
        "city": "Mau",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1127,
        "city": "Mavelikkara",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1117,
        "city": "Mavoor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 938,
        "city": "Mayiladuthurai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 441,
        "city": "Mayurbhanj",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 442,
        "city": "Medak",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1340,
        "city": "Medininagar",
        "state_id": 10,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 443,
        "city": "Medinipur",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 444,
        "city": "Meerut",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1354,
        "city": "Mehsana",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 946,
        "city": "Melmalayanur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 947,
        "city": "Melur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1277,
        "city": "Metpally",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 936,
        "city": "Mettupalayam",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 948,
        "city": "Mettur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 445,
        "city": "Mewat",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1045,
        "city": "Minicoy",
        "state_id": 34,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1442,
        "city": "Mira Bhayandar",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 446,
        "city": "Miraj",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1301,
        "city": "Miryalaguda",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 447,
        "city": "Mirzapur",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 949,
        "city": "Modakkurichi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 448,
        "city": "Moga",
        "state_id": 20,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 449,
        "city": "Mohali",
        "state_id": 20,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 950,
        "city": "Mohanur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 450,
        "city": "Mokokchung",
        "state_id": 18,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 451,
        "city": "Mon",
        "state_id": 18,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 452,
        "city": "Moradabad",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 453,
        "city": "Morbi",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 454,
        "city": "Morena",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 438,
        "city": "Morigaon",
        "state_id": 3,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1320,
        "city": "Motihari",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1197,
        "city": "Mudalgi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1138,
        "city": "Mudbidri",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1164,
        "city": "Muddebihal",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1230,
        "city": "Mudhol",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 953,
        "city": "Mudukulathur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1195,
        "city": "Mukkam",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 455,
        "city": "Muktsar",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1245,
        "city": "Mulbagal",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 456,
        "city": "Mumbai",
        "state_id": 14,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 457,
        "city": "Mungeli",
        "state_id": 5,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 458,
        "city": "Munger",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1019,
        "city": "Munnar",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 459,
        "city": "Murshidabad",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 951,
        "city": "Musiri",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1137,
        "city": "Muvattupuzha",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 460,
        "city": "Muzaffarnagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 461,
        "city": "Muzaffarpur",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 462,
        "city": "Mysuru",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 464,
        "city": "Nabarangapur",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 465,
        "city": "Nadia",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1377,
        "city": "Nadiad",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 466,
        "city": "Nagaon",
        "state_id": 3,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 467,
        "city": "Nagapattinam",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 468,
        "city": "Nagar Kurnool",
        "state_id": 24,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 469,
        "city": "Nagaur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1294,
        "city": "Nagda",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 770,
        "city": "Nagercoil",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 470,
        "city": "Nagpur",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1371,
        "city": "Naihati",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 471,
        "city": "Nainital",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 472,
        "city": "Nalanda",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 473,
        "city": "Nalbari",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 474,
        "city": "Nalgonda",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 954,
        "city": "Nallampalli",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 475,
        "city": "Namakkal",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 955,
        "city": "Nambiyur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 476,
        "city": "Nanded",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 477,
        "city": "Nandurbar",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1369,
        "city": "Nandyal",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1334,
        "city": "Nangloi Jat",
        "state_id": 32,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 957,
        "city": "Nanguneri",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 478,
        "city": "Nanjangud",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 774,
        "city": "Nanjikottai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 958,
        "city": "Nannilam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1314,
        "city": "Narasaraopet",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 479,
        "city": "Narayanpur",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1173,
        "city": "Nargund",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 480,
        "city": "Narmada",
        "state_id": 7,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1315,
        "city": "Narmadapuram",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 481,
        "city": "Narsinghpur",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 482,
        "city": "Nashik",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 775,
        "city": "Natham",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1462,
        "city": "Navi Mumbai",
        "state_id": 14,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 483,
        "city": "Navsari",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 484,
        "city": "Nawada",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 485,
        "city": "Nawanshahr",
        "state_id": 20,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 486,
        "city": "Nayagarh",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1249,
        "city": "Nedumangad",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 487,
        "city": "Neemuch",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1178,
        "city": "Nelamangala",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 776,
        "city": "Nellikuppam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 488,
        "city": "Nellore",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 489,
        "city": "New Delhi",
        "state_id": 32,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 777,
        "city": "Neyveli",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1268,
        "city": "Neyyattinkara",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 490,
        "city": "Nicobar",
        "state_id": 29,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 956,
        "city": "Nilakottai",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1212,
        "city": "Nilambur",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1238,
        "city": "Nileshwaram",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1255,
        "city": "Nipani",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 492,
        "city": "Nirmal",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 493,
        "city": "Nizamabad",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1441,
        "city": "Noida",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1031,
        "city": "Noney",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 494,
        "city": "North 24 Parganas",
        "state_id": 28,
        "price": 150,
        "top_ads_price": 50,
        "premium_ads_price": 40
      },
      {
        "id": 495,
        "city": "North And Middle Andaman",
        "state_id": 29,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 496,
        "city": "North Delhi",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1386,
        "city": "North Dumdum",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 498,
        "city": "North East Delhi",
        "state_id": 32,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 500,
        "city": "North Sikkim",
        "state_id": 22,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 501,
        "city": "North Tripura",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 502,
        "city": "North West Delhi",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 503,
        "city": "Nuapada",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 780,
        "city": "Oddanchatram",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1365,
        "city": "Ongole",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 778,
        "city": "Ooty",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1356,
        "city": "Orai",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 504,
        "city": "Osmanabad",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1235,
        "city": "Ottappalam",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 505,
        "city": "Pakur",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1088,
        "city": "Pala",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 506,
        "city": "Palakkad",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 507,
        "city": "Palakollu",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 508,
        "city": "Palamau",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 784,
        "city": "Palani",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1329,
        "city": "Palanpur",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 963,
        "city": "Palayamkottai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 509,
        "city": "Palghar",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 510,
        "city": "Pali",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 785,
        "city": "Palladam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 786,
        "city": "Pallapatti",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 787,
        "city": "Pallikonda",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 511,
        "city": "Palwal",
        "state_id": 8,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1282,
        "city": "Palwancha",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 788,
        "city": "Panagudi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 513,
        "city": "Panchkula",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 512,
        "city": "PanchMahals",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1223,
        "city": "Pandalam",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1415,
        "city": "Panihati",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 514,
        "city": "Panipat",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 515,
        "city": "Panna",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1247,
        "city": "Panoor",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 789,
        "city": "Panruti",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1433,
        "city": "Panvel",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 962,
        "city": "Papanasam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1159,
        "city": "Pappinisseri",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 959,
        "city": "Pappireddipatti",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 516,
        "city": "PapumPare",
        "state_id": 2,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 790,
        "city": "Paramakudi",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 965,
        "city": "Paramathi Velur",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 791,
        "city": "Parangipettai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1273,
        "city": "Parappanangadi",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1177,
        "city": "Paravur",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 517,
        "city": "Parbhani",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 518,
        "city": "Parkal",
        "state_id": 24,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 519,
        "city": "Paschim Bardhaman",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1396,
        "city": "Paschim Medinipur",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 520,
        "city": "Patan",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1464,
        "city": "Patancheru",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 521,
        "city": "Pathanamthitta",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 522,
        "city": "Pathankot",
        "state_id": 20,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 523,
        "city": "Patiala",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 524,
        "city": "Patna",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1129,
        "city": "Pattambi",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 792,
        "city": "Pattukkottai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 525,
        "city": "Pauri Garhwal",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1128,
        "city": "Pavagada",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1266,
        "city": "Payyanur",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1224,
        "city": "Payyoli",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 526,
        "city": "Peddapalli",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 960,
        "city": "Pennagaram",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1060,
        "city": "Peralasseri",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 527,
        "city": "Perambalur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 794,
        "city": "Peravurani",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 528,
        "city": "Peren",
        "state_id": 18,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1205,
        "city": "Perinthalmanna",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 795,
        "city": "Periyakulam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1024,
        "city": "Pernem",
        "state_id": 6,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1111,
        "city": "Perumbavoor",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 966,
        "city": "Perundurai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1316,
        "city": "Phagwara",
        "state_id": 20,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 529,
        "city": "Phek",
        "state_id": 18,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1217,
        "city": "Pherzawl",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1288,
        "city": "Phusro",
        "state_id": 10,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 530,
        "city": "Pilibhit",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1456,
        "city": "Pimpri Chinchwad",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1061,
        "city": "Pinarayi",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1135,
        "city": "Piravom",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1321,
        "city": "Pithampur",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 531,
        "city": "Pithoragarh",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 970,
        "city": "Pochampalli",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 798,
        "city": "Pollachi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 799,
        "city": "Polur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 967,
        "city": "Ponnamaravathi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1289,
        "city": "Ponnani",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 800,
        "city": "Ponneri",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 532,
        "city": "Poonch",
        "state_id": 35,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 533,
        "city": "Porbandar",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 534,
        "city": "Port Blair",
        "state_id": 29,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1041,
        "city": "Pottore",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 535,
        "city": "Prakasam",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 536,
        "city": "Pratapgarh",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1370,
        "city": "Proddatur",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 538,
        "city": "Puducherry",
        "state_id": 36,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 539,
        "city": "Pudukkottai",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 802,
        "city": "Pudupattinam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 803,
        "city": "Puliyankudi",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 540,
        "city": "Pulwama",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1216,
        "city": "Punalur",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 541,
        "city": "Pune",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1411,
        "city": "Purba Bardhaman",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1361,
        "city": "Purba Medinipur",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 542,
        "city": "Puri",
        "state_id": 19,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 543,
        "city": "Purnia",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 544,
        "city": "Puruliya",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1052,
        "city": "Puthukkad",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 973,
        "city": "Radhapuram",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 545,
        "city": "Raebareli",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 546,
        "city": "Raichur",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1475,
        "city": "Raigad",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1352,
        "city": "Raiganj",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 547,
        "city": "Raigarh",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 548,
        "city": "Raipur",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 549,
        "city": "Raisen",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1029,
        "city": "Rajahmundry",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 805,
        "city": "Rajapalayam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 550,
        "city": "Rajauri",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 551,
        "city": "Rajgarh",
        "state_id": 13,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 552,
        "city": "Rajkot",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 553,
        "city": "Rajnandgaon",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1420,
        "city": "Rajpur Sonarpur",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 554,
        "city": "Rajsamand",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1384,
        "city": "Ramagundam",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 555,
        "city": "Ramanagara",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 556,
        "city": "Ramanathapuram",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1170,
        "city": "Ramanattukara",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 557,
        "city": "Ramban",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 558,
        "city": "Ramdurg",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 807,
        "city": "Rameshwaram",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 559,
        "city": "Ramgarh",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 560,
        "city": "Rampur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 561,
        "city": "Ranchi",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 562,
        "city": "Rangareddy",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1303,
        "city": "Ranibennur",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 808,
        "city": "Rasipuram",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 563,
        "city": "Ratlam",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 564,
        "city": "Ratnagiri",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 565,
        "city": "Rayagada",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 566,
        "city": "Reasi",
        "state_id": 35,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 567,
        "city": "Rewa",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 568,
        "city": "Rewari",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 569,
        "city": "Ri Bhoi",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1341,
        "city": "RobertsonPet",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 570,
        "city": "Rohtak",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 571,
        "city": "Rohtas",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 572,
        "city": "Ropar",
        "state_id": 20,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1402,
        "city": "Rourkela",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 573,
        "city": "Rudraprayag",
        "state_id": 27,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 575,
        "city": "Sabarkantha",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 576,
        "city": "Sagar",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 577,
        "city": "Saharanpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 578,
        "city": "Saharsa",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 579,
        "city": "Sahibganj",
        "state_id": 10,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 580,
        "city": "Saiha",
        "state_id": 17,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1099,
        "city": "Sakleshpur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 581,
        "city": "Salem",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 582,
        "city": "Samastipur",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 583,
        "city": "Samba",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 584,
        "city": "Sambalpur",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 585,
        "city": "Sambhal",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1179,
        "city": "Sandur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 976,
        "city": "Sangagiri",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 586,
        "city": "Sangareddy",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 587,
        "city": "Sangli",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 588,
        "city": "Sangrur",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 810,
        "city": "Sankarankoil",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 589,
        "city": "Sant Kabir Nagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 591,
        "city": "Saran",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 592,
        "city": "Saraswathipuram",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 593,
        "city": "Satara",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 975,
        "city": "Sathankulam",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 812,
        "city": "Sathyamangalam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 594,
        "city": "Satna",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 813,
        "city": "Sattur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 595,
        "city": "Sawai Madhopur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 596,
        "city": "Secunderabad",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 597,
        "city": "Sehore",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 598,
        "city": "Senapati",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 979,
        "city": "Sendamangalam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 599,
        "city": "Seoni",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 600,
        "city": "Sepahijala",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 601,
        "city": "Seraikela Kharsawan",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1350,
        "city": "Serampore",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 602,
        "city": "Serchhip",
        "state_id": 17,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 603,
        "city": "Shahdara",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 604,
        "city": "Shahdol",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 605,
        "city": "Shahjahanpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 606,
        "city": "Shajapur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1333,
        "city": "Shamli",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 607,
        "city": "Sheikhpura",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 814,
        "city": "Shenkottai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 608,
        "city": "Sheohar",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 609,
        "city": "Sheopur",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 610,
        "city": "Shillong",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 611,
        "city": "Shimla",
        "state_id": 9,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 612,
        "city": "Shivamogga",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 613,
        "city": "Shivpuri",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 816,
        "city": "Sholingur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 978,
        "city": "Shoolagiri",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 614,
        "city": "Shopian",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1198,
        "city": "Shoranur",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 615,
        "city": "Shravasti",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 616,
        "city": "Shrirampur",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1103,
        "city": "Shrirangapattana",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 617,
        "city": "Sibsagar",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 618,
        "city": "Siddapur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 619,
        "city": "Siddharthnagar",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1311,
        "city": "Siddipet",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 621,
        "city": "Sidhi",
        "state_id": 13,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1226,
        "city": "Sidlaghatta",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 622,
        "city": "Sikar",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1479,
        "city": "Silchar",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1426,
        "city": "Siliguri",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 623,
        "city": "Simdega",
        "state_id": 10,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 624,
        "city": "Sindhudurg",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 980,
        "city": "Singampunari",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 625,
        "city": "Singrauli",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1285,
        "city": "Sircilla",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 817,
        "city": "Sirkali",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 627,
        "city": "Sirmaur",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 628,
        "city": "Sirohi",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 629,
        "city": "Sirsa",
        "state_id": 8,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1476,
        "city": "Sirsi",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1261,
        "city": "Siruguppa",
        "state_id": 11,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 630,
        "city": "Sitamarhi",
        "state_id": 4,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 631,
        "city": "Sitapur",
        "state_id": 26,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 632,
        "city": "Sivaganga",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 819,
        "city": "Sivagiri",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 820,
        "city": "Sivakasi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 633,
        "city": "Siwan",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 634,
        "city": "Solan",
        "state_id": 9,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 635,
        "city": "Solapur",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 636,
        "city": "Sonapur",
        "state_id": 3,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 637,
        "city": "Sonbhadra",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1440,
        "city": "Sonepur",
        "state_id": 19,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 638,
        "city": "Sonipat",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 639,
        "city": "Sonitpur",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1274,
        "city": "Sopore",
        "state_id": 35,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 640,
        "city": "South 24 Parganas",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 641,
        "city": "South Andaman",
        "state_id": 29,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 642,
        "city": "South Delhi",
        "state_id": 32,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1419,
        "city": "South Dumdum",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 644,
        "city": "South Garo Hills",
        "state_id": 16,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 646,
        "city": "South Sikkim",
        "state_id": 22,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 647,
        "city": "South Tripura",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 648,
        "city": "South West Delhi",
        "state_id": 32,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 649,
        "city": "South West Khasi Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1161,
        "city": "Sreekandapuram",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 650,
        "city": "Sri Ganganagar",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 651,
        "city": "Srikakulam",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 652,
        "city": "Srikalahasti",
        "state_id": 1,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 653,
        "city": "Srinagar",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1112,
        "city": "Srinivaspur",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 821,
        "city": "Srivilliputhur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 654,
        "city": "Stn Jadcherla",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 655,
        "city": "Sukma",
        "state_id": 5,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1208,
        "city": "Sultan Bathery",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1343,
        "city": "Sultan Pur Majra",
        "state_id": 32,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 656,
        "city": "Sultanpur",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 657,
        "city": "Sundergarh",
        "state_id": 19,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 658,
        "city": "Supaul",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 659,
        "city": "Surajpur",
        "state_id": 5,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 822,
        "city": "Surandai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 660,
        "city": "Surat",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 661,
        "city": "Surendra Nagar",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 662,
        "city": "Surguja",
        "state_id": 5,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1304,
        "city": "Suryapet",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 664,
        "city": "Tadepalligudem",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1306,
        "city": "Tadipatri",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1263,
        "city": "Taliparamba",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 665,
        "city": "Tamenglong",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1258,
        "city": "Tandur",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1269,
        "city": "Tanur",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1171,
        "city": "Tarikere",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 667,
        "city": "Tarn Taran",
        "state_id": 20,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 668,
        "city": "Tawang",
        "state_id": 2,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 669,
        "city": "Tehri Garhwal",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1345,
        "city": "Tenali",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 670,
        "city": "Tengnoupal",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 824,
        "city": "Tenkasi",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 671,
        "city": "Thalassery",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 672,
        "city": "Thane",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 673,
        "city": "Thanjavur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 674,
        "city": "Thanlon",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 827,
        "city": "Tharamangalam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 828,
        "city": "Tharangambadi",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 675,
        "city": "Theni",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 829,
        "city": "Thirumangalam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 830,
        "city": "Thirunindravur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 992,
        "city": "Thirupparankundram",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 993,
        "city": "Thiruppuvanam",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 833,
        "city": "Thiruthuraipoondi",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 994,
        "city": "Thiruvaiyaru",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1243,
        "city": "Thiruvalla",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 834,
        "city": "Thiruvallur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 676,
        "city": "Thiruvananthapuram",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 835,
        "city": "Thiruvarur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 995,
        "city": "Thiruvennainallur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 988,
        "city": "Thisayanvilai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1211,
        "city": "Thodupuzha",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 836,
        "city": "Thoothukudi",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 997,
        "city": "Thottiyam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 677,
        "city": "Thoubal",
        "state_id": 15,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 996,
        "city": "Thovalai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1259,
        "city": "Thrikkakkara",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1290,
        "city": "Thrippunithura",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 678,
        "city": "Thrissur",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 837,
        "city": "Thuraiyur",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 679,
        "city": "Tikamgarh",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 838,
        "city": "Tindivanam",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 680,
        "city": "Tinsukia",
        "state_id": 3,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1375,
        "city": "Tiptur",
        "state_id": 11,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 681,
        "city": "Tirap",
        "state_id": 2,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 839,
        "city": "Tiruchendur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 840,
        "city": "Tiruchengode",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 682,
        "city": "Tiruchirappalli",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 987,
        "city": "Tirukkoyilur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 683,
        "city": "Tirunelveli",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 845,
        "city": "Tirupathur",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1020,
        "city": "Tirupati",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 684,
        "city": "Tiruppur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1234,
        "city": "Tirur",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 847,
        "city": "Tiruttani",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 986,
        "city": "Tiruvadanai",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1232,
        "city": "Tiruvalla",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 685,
        "city": "Tiruvallur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 686,
        "city": "Tiruvannamalai",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 687,
        "city": "Tiruvarur",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 688,
        "city": "Tonk",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 690,
        "city": "Tuensang",
        "state_id": 18,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 691,
        "city": "Tumakuru",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 692,
        "city": "Tura",
        "state_id": 16,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 694,
        "city": "Udaipur",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1427,
        "city": "Udaipur",
        "state_id": 21,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 695,
        "city": "Udalguri",
        "state_id": 3,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1299,
        "city": "Udgir",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 696,
        "city": "Udham Singh Nagar",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 697,
        "city": "Udhampur",
        "state_id": 35,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 852,
        "city": "Udumalaipettai",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 698,
        "city": "Udupi",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 699,
        "city": "Ujjain",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 700,
        "city": "Ukhrul",
        "state_id": 15,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1432,
        "city": "Ulhasnagar",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1379,
        "city": "Uluberia",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 999,
        "city": "Ulundurpet",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 701,
        "city": "Umaria",
        "state_id": 13,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 702,
        "city": "Una",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1437,
        "city": "Una",
        "state_id": 9,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1399,
        "city": "Unakoti",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 703,
        "city": "Unnao",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 704,
        "city": "Upper Dibang Valley",
        "state_id": 2,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 705,
        "city": "Upper Siang",
        "state_id": 2,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 706,
        "city": "Upper Subansiri",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1000,
        "city": "Uthangarai",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1002,
        "city": "Uthukuli",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1359,
        "city": "Uttar Dinajpur",
        "state_id": 28,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 707,
        "city": "Uttara Kannada",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 708,
        "city": "Uttarkashi",
        "state_id": 27,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1407,
        "city": "Uzhavarkarai",
        "state_id": 36,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1319,
        "city": "Vadakara",
        "state_id": 12,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 709,
        "city": "Vadodara",
        "state_id": 7,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1094,
        "city": "Vaikom",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 710,
        "city": "Vaishali",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 860,
        "city": "Valparai",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 711,
        "city": "Valsad",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 861,
        "city": "Vandavasi",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 862,
        "city": "Vaniyambadi",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1342,
        "city": "Vapi",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 712,
        "city": "Varanasi",
        "state_id": 26,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1196,
        "city": "Varkala",
        "state_id": 12,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1451,
        "city": "Vasai Virar",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1283,
        "city": "Vatakara",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 863,
        "city": "Vedaranyam",
        "state_id": 23,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 864,
        "city": "Vellakoil",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 713,
        "city": "Vellore",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1339,
        "city": "Veraval",
        "state_id": 7,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 714,
        "city": "Vidisha",
        "state_id": 13,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1405,
        "city": "Vijayapura",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 1025,
        "city": "Vijayawada",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 715,
        "city": "Vikarabad",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 867,
        "city": "Viluppuram",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 868,
        "city": "Virudhachalam",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 717,
        "city": "Virudhunagar",
        "state_id": 23,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 718,
        "city": "Visakhapatnam",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 719,
        "city": "Vizianagaram",
        "state_id": 1,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1254,
        "city": "Wadakkancherry",
        "state_id": 12,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1104,
        "city": "Wadi",
        "state_id": 11,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1016,
        "city": "Walajabad",
        "state_id": 23,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      },
      {
        "id": 1253,
        "city": "Wanaparthy",
        "state_id": 24,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1443,
        "city": "Warangal",
        "state_id": 24,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 722,
        "city": "Wardha",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 723,
        "city": "Washim",
        "state_id": 14,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 724,
        "city": "Wayanad",
        "state_id": 12,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 725,
        "city": "West Champaran",
        "state_id": 4,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 726,
        "city": "West Delhi",
        "state_id": 32,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 727,
        "city": "West Garo Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 728,
        "city": "West Godavari",
        "state_id": 1,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 729,
        "city": "West Jaintia Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 730,
        "city": "West Kameng",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 731,
        "city": "West Khasi Hills",
        "state_id": 16,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 732,
        "city": "West Midnapore",
        "state_id": 28,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 733,
        "city": "West Siang",
        "state_id": 2,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 734,
        "city": "West Sikkim",
        "state_id": 22,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 735,
        "city": "West Singhbhum",
        "state_id": 10,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 736,
        "city": "West Tripura",
        "state_id": 25,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 737,
        "city": "Wokha",
        "state_id": 18,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 738,
        "city": "Yadgir",
        "state_id": 11,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 739,
        "city": "Yamunanagar",
        "state_id": 8,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 740,
        "city": "Yanam",
        "state_id": 36,
        "price": 100,
        "top_ads_price": 40,
        "premium_ads_price": 30
      },
      {
        "id": 741,
        "city": "Yavatmal",
        "state_id": 14,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 1017,
        "city": "Yercaud",
        "state_id": 23,
        "price": 50,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 742,
        "city": "Zaheerabad",
        "state_id": 24,
        "price": 75,
        "top_ads_price": 25,
        "premium_ads_price": 20
      },
      {
        "id": 743,
        "city": "Zunheboto",
        "state_id": 18,
        "price": 25,
        "top_ads_price": 10,
        "premium_ads_price": 10
      }
]
   
new_cities = []

for city in cities:

    dic_ = {
        "city_id": str(city["id"]),
        "city_name": city['city']
    }

    new_cities.append(dic_)


with open('city.json', 'w') as f:

    dump(new_cities, f)