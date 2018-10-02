import xml.etree.ElementTree as ET

class gexf_file:

    def __init__(self):
        self.gexf = ET.Element("gexf")
        self.meta = ET.SubElement(self.gexf, "meta")
        self.creator = ET.SubElement(self.meta, "creator")
        self.creator.text = "the_influencer"
        self.description = ET.SubElement(self.meta, "description")
        self.description.text = "This file represents a Software Ecosystem and the influence relation between their " \
                                "components"
        self.graph = ET.SubElement(self.gexf, "graph")
        self.nodes = ET.SubElement(self.graph, "nodes")
        self.edges = ET.SubElement(self.graph, "edges")

    def insert_node_ecosystem(self, ecosystem):
        self.node = ET.SubElement(self.nodes, "node")
        self.node.set("id", ecosystem.ecosystem_name)
        self.node.set("label", ecosystem.ecosystem_name)

    def insert_node_project_ecosystem(self, project, ecosystem):
        self.node = ET.SubElement(self.nodes, "node")
        self.node.set("id", project.name)
        self.node.set("label", project.name)
        self.edge = ET.SubElement(self.edges, "edge")
        self.edge.set("id", project.project_name + "_" + ecosystem.ecosystem_name)
        self.edge.set("source", project.project_name)
        self.edge.set("target", ecosystem.ecosystem_name)

    def insert_node_project(self, project):
        self.node = ET.SubElement(self.nodes, "node")
        self.node.set("id", project.name)
        self.node.set("label", project.name)

    def insert_node_user(self, user, project):
        self.node = ET.SubElement(self.nodes, "node")
        self.node.set("id", user.user_name)
        self.node.set("label", user.user_name)
        self.edge = ET.SubElement(self.nodes, "edge")
        self.edge.set("id", user.user_name + "_" + project.project_name)
        self.edge.set("source", user.user_name)
        self.edge.set("target", project.project_name)

    def write_file(self, gexf_result_file_path):
        gexf_data = ET.tostring(self.gexf)
        gexf_result_file = gexf_result_file_path

