import read_html, config

def _main(url):
    site = read_html.Find_text(url, config.file_name_setting)
    text = site.find_text()
    site.write_text_to_file(text)
    file_name = site.new_dir + site.new_name
    format_text = read_html.Formating_file(file_name)
    format_text.width_of_string()

if __name__ == '__main__':
    if isinstance(config.urls, list):
        for i in config.urls:
            _main(i)
    else:
        _main(config.urls)





