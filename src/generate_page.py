import os

from markdown_to_html_node import markdown_to_html_node
from htmlnode import HTMLNode


def extract_title(markdown):
    header = markdown.split("\n")[0]
    if not header.startswith("#"):
        raise Exception(f"h1 header not found in markdown: {header}")
    if header.startswith("##"):
        raise Exception(f"Not an h1 header")
    header = header.strip("#")
    header = header.strip()
    return header


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from: {from_path} to {dest_path} using template: {template_path}")
    markdown_file = None
    template_file = None
    html_file = None
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_file = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template_file = f.read()

    html_file = markdown_to_html_node(markdown_file)
    html_file = html_file.to_html()
    title = extract_title(markdown_file)
    generated_page = (((template_file.
                        replace("{{ Title }}", title).
                        replace("{{ Content }}", html_file)).
                       replace('href="/', f'href="{basepath}')).
                      replace('src="/', f'src="{basepath}'))
    if not os.path.exists(dest_path.replace(f"/{dest_path.split('/')[-1]}", "")):
        os.makedirs(dest_path.replace(f"/{dest_path.split('/')[-1]}", ""))
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(generated_page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content = os.listdir(dir_path_content)
    print(content)
    for item in content:
        if item.endswith(".md:"):
            continue
        if os.path.isdir(os.path.join(dir_path_content, item)):
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path,
                                     os.path.join(dest_dir_path, item), basepath)
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(os.path.join(dir_path_content, item), template_path,
                          os.path.join(dest_dir_path, item.replace(".md", ".html")), basepath)
