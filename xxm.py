image_info = [
{
    "id" : "34694102243_3370955cf9_z",
    "title" : "Eastern",
    "flickr_user" : "Sean Davis",
    "tags" : ["Los Angeles", "California", "building"]
},
{
    "id" : "37198655640_b64940bd52_z",
    "title" : "Spreetunnel",
    "flickr_user" : "Jens-Olaf Walter",
    "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
},
{
    "id" : "36909037971_884bd535b1_z",
    "title" : "East Side Gallery",
    "flickr_user" : "Pieter van der Velden",
    "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
},
{
    "id" : "36604481574_c9f5817172_z",
    "title" : "Lombardia, september 2017",
    "flickr_user" : "Mónica Pinheiro",
    "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
}
]

x = image_info[0]["title"][1]
y = image_info[2]["tags"][1][1]

print(y == x)
