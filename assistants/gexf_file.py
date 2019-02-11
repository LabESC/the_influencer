import xml.etree.ElementTree as ET

class gexf_file:

    def __init__(self):
        self.gexf = ET.Element("gexf")
        self.gexf.set("xmlns", "http://www.gexf.net/1.2draft")
        self.gexf.set("xmlns:viz", "http://www.gexf.net/1.1draft/viz")
        self.gexf.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        self.gexf.set("xsi:schemaLocation", "http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd")
        self.gexf.set("version", "1.2")
        self.meta = ET.SubElement(self.gexf, "meta")
        self.creator = ET.SubElement(self.meta, "creator")
        self.creator.text = "the_influencer"
        self.description = ET.SubElement(self.meta, "description")
        self.description.text = "This file represents a Software Ecosystem and the influence relation between their " \
                                "components"
        self.graph = ET.SubElement(self.gexf, "graph")
        self.graph.set("mode", "static")
        self.graph.set("defaultedgetype", "undirected")
        self.nodes = ET.SubElement(self.graph, "nodes")
        self.edges = ET.SubElement(self.graph, "edges")

    def insert_node_ecosystem(self, ecosystem):
        node = ET.SubElement(self.nodes, "node")
        node.set("id", ecosystem.ecosystem_name)
        node.set("label", ecosystem.ecosystem_name)
        node_color = ET.SubElement(node, "viz:color")
        node_color.set("r", "255")
        node_color.set("g", "0")
        node_color.set("b", "0")
        node_color.set("a", "1")
        node_size = ET.SubElement(node, "viz:size")
        node_size.set("value", str(ecosystem.total_ecosystem_influence))


    def insert_node_project_ecosystem(self, project, ecosystem):
        node = ET.SubElement(self.nodes, "node")
        node.set("id", project.project_name)
        node.set("label", project.project_name)
        node_color = ET.SubElement(node, "viz:color")
        node_color.set("r", "0")
        node_color.set("g", "255")
        node_color.set("b", "0")
        node_color.set("a", "1")
        node_size = ET.SubElement(node, "viz:size")
        node_size.set("value", str(project.total_project_influence))
        edge = ET.SubElement(self.edges, "edge")
        edge.set("id", project.project_name + "_" + ecosystem.ecosystem_name)
        edge.set("source", project.project_name)
        edge.set("target", ecosystem.ecosystem_name)

    def insert_node_project(self, project):
        node = ET.SubElement(self.nodes, "node")
        node.set("id", project.project_name)
        node.set("label", project.project_name)
        node_color = ET.SubElement(node, "viz:color")
        node_color.set("r", "0")
        node_color.set("g", "255")
        node_color.set("b", "0")
        node_color.set("a", "1")
        node_size = ET.SubElement(node, "viz:size")
        node_size.set("value", str(project.total_project_influence))

    def insert_node_user(self, user, project):
        node = ET.SubElement(self.nodes, "node")
        node.set("id", user.user_name)
        node.set("label", user.user_name)
        node_color = ET.SubElement(node, "viz:color")
        node_color.set("r", "0")
        node_color.set("g", "0")
        node_color.set("b", "255")
        node_color.set("a", "1")
        node_size = ET.SubElement(node, "viz:size")
        node_size.set("value", str(user.project_influence_level))
        edge = ET.SubElement(self.edges, "edge")
        edge.set("id", user.user_name + "_" + project.project_name)
        edge.set("source", user.user_name)
        edge.set("target", project.project_name)

    def verify_node_user_existence(self, user):
        if self.gexf.iselement(user.user_name):
            return True
        return False

    def write_file(self, gexf_result_file_path):
        gexf_data = ET.tostring(self.gexf)
        gexf_data = str(gexf_data, "utf-8")
        gexf_file = open(gexf_result_file_path + ".gexf", "w")
        print(type(gexf_data))
        gexf_file.write(gexf_data)

