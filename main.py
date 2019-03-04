import read_html, config

def _main(url):
    site = read_html.Find_text(url, config.file_name_setting)
    text = site.find_text()
    site.write_text_to_file(text)
    text = read_html.Formating_file(url, config.file_name_setting)
    text.width_of_string()

if __name__ == '__main__':
    if isinstance(config.urls, list):
        for i in config.urls:
            _main(i)
    else:
        _main(config.urls)





