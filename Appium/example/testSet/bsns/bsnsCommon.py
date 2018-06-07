activity = {}
def setXml():
    """
    get the xml file's value
    :use:
    a = getXml(path)

    print(a.get(".module.GuideActivity").get("skip").get("type"))
    :param: xmlPath
    :return:activity
    """
    if len(activity) == 0:
        xmlPath = os.path.join(readConfig.prjDir, "testSet\\bsns", "element.xml")
        # open the xml file
        per = ET.parse(xmlPath)
        allElement = per.findall('activity')

        for firstElement in allElement:
            activityName = firstElement.get("name")

            element = {}
            for secondElement in firstElement.getchildren():
                elementName = secondElement.get("name")

                elementChild = {}
                for thirdElement in secondElement.getchildren():

                    elementChild[thirdElement.tag] = thirdElement.text

                element[elementName] = elementChild
            activity[activityName] = element

def getElDict(activityName, elementName):
    """
    According to the activityName and elementName get element
    :param activityNmae:
    :param elementName:
    :return:
    """
    setXml()
    elementDict = activity.get(activityName).get(elementName)
    return elementDict

class element:

    def __init__(self, activutyName, elementName):
        global driver
        driver = myDriver.GetDriver()
        self.activutyNmae = activutyNmae
        self.elementName = elementName
        elementDict = getElDict(self.activutyNmae, self.elementName)
        self.pathtype = elementDict.get("pathtype")
        self.pathvalue = elementDict.get("pathvalue")

    def isExist(self):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """
        try:
            if self.pathtype == "ID":
                driver.find_element_by_id(self.pathvalue)
            if self.pathtype == "CLASSNAME":
                driver.find_element_by_class_name(self.pathvalue)
            if self.pathtype == "XPATH":
                driver.find_element_by_xpath(self.pathvalue)
            if self.pathtype == "NAME":
                driver.find_element_by_name(self.pathvalue)
        except NoSuchElementException:
            return False
        return True

    def doesExist(self):
        """
        To determine whether an element is exits
        :return:
        """
        i = 1
        while not self.isExist():
            sleep(1)
            i = i+1
            if i >= 10:
                return False
        else:
            return True

    def get(self):
        """
        get one element
        :return:
        """
        if self.doesExist():
            if self.pathtype == "ID":
                element = driver.find_element_by_id(self.pathvalue)
                return element
            if self.pathtype == "CLASSNAME":
                element = driver.find_element_by_class_name(self.pathvalue)
                return element
            if self.pathtype == "XPATH":
                element = driver.find_element_by_xpath(self.pathvalue)
                return element
            if self.pathtype == "NAME":
                element = driver.find_element_by_name(self.pathvalue)
                return element
        else:
            return None

    def gets(self, index):
        """
        get one element in elementList
        :return:
        """
        if self.doesExist():
            if self.pathtype == "ID":
                elements = driver.find_elements_by_id(self.pathvalue)
                return elements[index]
            if self.pathtype == "CLASSNAME":
                elements = driver.find_elements_by_class_name(self.pathvalue)
                return elements[index]
            if self.pathtype == "XPATH":
                elements = driver.find_elements_by_xpath(self.pathvalue)
                return elements[index]
            if self.pathtype == "NAME":
                elements = driver.find_elements_by_name(self.pathvalue)
                return elements[index]
            return None
        else:
            return None

    def click(self):
        """
        click element
        :return:
        """
        try:
            el = self.get()
            el.click()
        except AttributeError:
            raise

    def clicks(self, index):
        """
        click element
        :return:
        """
        try:
            el = self.gets(index)
            el.click()
        except AttributeError:
            raise

    def sendKey(self,values):
        """
        input the key
        :return:
        """
        try:
            el = self.get()
            el.clear()
            el.send_keys(values)
        except AttributeError:
            raise

    def sendKeys(self, index, values):
        """
        input the key
        :return:
        """
        try:
            el = self.gets(index)
            el.clear()
            el.send_keys(values)
        except AttributeError:
            raise

    def getAttribute(self, attribute):
        """
        get the element attribute
        :param attribute:
        :return:value
        """
        el = self.get()
        value = el.get_attribute(attribute)
        return value