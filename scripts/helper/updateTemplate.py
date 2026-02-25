def updateTemplate(key, template, updateValue):
    return template.replace("{{" + key + "}}", str(updateValue))