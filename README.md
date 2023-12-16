[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-Pinterest

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GBYJUrAaIAAUKCb.jpeg)

Proyek ini menggunakan API [Pinterest](https://pinterest.com/) untuk melakukan web scraping dan mengambil gambar berdasarkan </br>keyword pencarian. Dengan memanfaatkan fungsionalitas API [Pinterest](https://pinterest.com/), program ini dapat secara </br>otomatis mengumpulkan gambar yang sesuai dengan keyword yang dimasukkan oleh pengguna. Pengguna </br>dapat menjalankan program, memberikan kata kunci pencarian, dan mendapatkan kumpulan gambar yang </br>relevan dari [Pinterest](https://pinterest.com/). Pastikan untuk mematuhi kebijakan penggunaan API [Pinterest](https://pinterest.com/) dan hak cipta </br>gambar yang diambil dalam pengembangan proyek ini.

## Requirements

- **Python >= 3.11.4**
- **Requests >= 2.31.0**
- **pytz >= 2023.3.post1**

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/craw-Pinterest

# Change Directory
cd craw-Pinterest

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

```bash
python main.py --keyword=Freya --size=10 --download=True --output=data
```

### Flags

| Flag       | Alias |          Description          | Example         | Default |
| :--------- | :---: | :---------------------------: | :-------------- | :-----: |
| --keyword  |  -k   | keywords to search for images | --keyword=Freya |  Freya  |
| --size     |  -s   |      size of image data       | --size=10       |   10    |
| --download |  -d   |        download image         | --download=True |  False  |
| --output   |  -o   |     json file output path     | --output=data   |  data   |

## Sample Output

```json
{
  "date_now": "2023-12-15T23:30:27",
  "keyword": "Freya",
  "size": 10,
  "data": [
    {
      "id": "165718461281756936",
      "created_at": "2023-10-21T00:04:27",
      "domain": "Uploaded by user",
      "link_pin": "https://www.pinterest.com/pin/165718461281756936",
      "link": null,
      "title": "💗",
      "description": " ",
      "media": {
        "images": {
          "170x": {
            "width": 236,
            "height": 419,
            "url": "https://i.pinimg.com/236x/aa/7b/6b/aa7b6bd53eb2759b1a0a7e9629532d31.jpg"
          },
          "236x": {
            "width": 236,
            "height": 419,
            "url": "https://i.pinimg.com/236x/aa/7b/6b/aa7b6bd53eb2759b1a0a7e9629532d31.jpg"
          },
          "474x": {
            "width": 474,
            "height": 842,
            "url": "https://i.pinimg.com/474x/aa/7b/6b/aa7b6bd53eb2759b1a0a7e9629532d31.jpg"
          },
          "736x": {
            "width": 736,
            "height": 1308,
            "url": "https://i.pinimg.com/736x/aa/7b/6b/aa7b6bd53eb2759b1a0a7e9629532d31.jpg"
          },
          "orig": {
            "width": 736,
            "height": 1308,
            "url": "https://i.pinimg.com/originals/aa/7b/6b/aa7b6bd53eb2759b1a0a7e9629532d31.jpg"
          }
        },
        "videos": null
      }
    }
    // more data
  ]
}
```

## License

This project is licensed under the [MIT License](LICENSE).
