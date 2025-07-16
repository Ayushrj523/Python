name = input("Enter your name: ")
bio = input("Write a short note about you: ")

print("\nEnter your skills (separated by commas):")
skills_input = input("Skills: ")
skills = [skill.strip() for skill in skills_input.split(",")]

print("\nEnter your projects (name and description):")
projects = []
while True:
    project_name = input("Project Name (leave empty to finish): ")
    if project_name == "":
        break
    project_desc = input("Project Description: ")
    projects.append((project_name, project_desc))

md_content = f"# {name}'s Portfolio\n\n"
md_content += f"## About Me\n{bio}\n\n"
md_content += "## Skills\n"
for skill in skills:
    md_content += f"- {skill}\n"

md_content += "\n## Projects\n"
for pname, pdesc in projects:
    md_content += f"### {pname}\n{pdesc}\n\n"

with open("portfolio.md", "w") as file:
    file.write(md_content)

print("\n✅ Portfolio generated as 'portfolio.md'. You can copy-paste it into your GitHub profile!")
