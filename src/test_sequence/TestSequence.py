import unittest
from parameterized import parameterized
import sys
sys.path.append("..")
from activity_diagram.ActivityDiagram import ActivityDiagram
from activity_diagram_elements.ActivityDiagramElements import ActivityDiagramElements
from activity_diagram_transitions.ActivityDiagramTransitions import ActivityDiagramTransitions
from activity_node.ActivityNode import ActivityNode
from decision_node.DecisionNode import DecisionNode
from final_node.FinalNode import FinalNode
from fragment.Fragment import Fragment
from fragments.Fragments import Fragments
from life_line.Lifeline import Lifeline
from life_lines.Lifelines import Lifelines
from merge_node.MergeNode import MergeNode
from message.Message import Message
from optional.Optional import Optional
from sequence_diagram.SequenceDiagram import SequenceDiagram
from sequence_diagrams.SequenceDiagrams import SequenceDiagrams
from start_node.StartNode import StartNode
from transition.Transition import Transition
class TestSequence(unittest.TestCase):
    # Diagrama de Atividades
    
    AD = ActivityDiagram()
    AD.set_attr({'name': 'nome do diagrama'})
    
    # Elementos
    
    ADE = ActivityDiagramElements()
    ADE.set_attr({'name': 'nome do bloco de elementos'})
    
    SN = StartNode()
    SN.set_attr({'name': 'nome do bloco inicial'})
    
    AN = ActivityNode()
    AN.set_attr({'name': 'nome da atividade'})
    
    DN = DecisionNode()
    DN.set_attr({'name': 'nome do nó de decisão'})
    
    MN = MergeNode()
    MN.set_attr({'name': 'nome do nó de fusão'})
    
    FN = FinalNode()
    FN.set_attr({'name': 'nome do nó final'})
    
    ADE.add_children([SN, AN, DN, MN, FN])
    
    # Transições
    ADT = ActivityDiagramTransitions()
    ADT.set_attr({'name': 'nome do nó de transições'})
    T1 = Transition([SN], [AN])
    T2 = Transition([AN], [DN])
    T3 = Transition([DN], [MN])
    T4 = Transition([MN], [FN])
    
    ADT.add_children([T1, T2, T3, T4])
    
    # Diagrama
    AD.add_child(ADE)
    AD.add_child(ADT)
    
    # Diagrama de Sequência
    SDS = SequenceDiagrams()
    
    LS = Lifelines()
    
    L = Lifeline()
    L.set_attr({'name': 'nome da lifeline'})
    
    FS = Fragments()
    
    O = Optional()
    O.set_attr({'name': 'nome do fragmento', 'representedBy': 'nome do diagrama de sequencia'})
    
    SD = SequenceDiagram()
    SD.set_attr({'name': 'nome do diagrama'})
    
    M = Message()
    M.set_attr({'name': 'nome da mensagem', 'prob': 'valor da probabilidade', 'source': 'nome da lifeline', 'target': 'nome da lifeline'})
    
    F = Fragment()
    F.set_attr({'name': 'nome da mensagem', 'prob': 'valor da probabilidade'})
    
    
    
    LS.add_children([L, L, L])
    FS.add_children([O, O, O])
    SD.add_children([M, M, F, M])
    SDS.add_children([LS, FS, SD, SD])
    
    file_AD = open(AD.attr['name']+'.txt', "w")
    file_AD.write(AD.get_child_xml())
    file_AD.close()
    file_SDS = open('Sequence Diagram.txt', "w")
    file_SDS.write(SDS.get_child_xml())
    file_SDS.close()
    
    @parameterized.expand([
        ["teste 1", SN, "<StartNode id=3 name='nome do bloco inicial'/>"],
        ["teste 2", ADE, "<ActivityDiagramElements name='nome do bloco de elementos'>\n<StartNode id=3 name='nome do bloco inicial'/>\n<ActivityNode id=4 name='nome da atividade'/>\n<DecisionNode id=5 name='nome do nó de decisão'/>\n<MergeNode id=6 name='nome do nó de fusão'/>\n<FinalNode id=7 name='nome do nó final'/>\n</ActivityDiagramElements>"],
        ["teste 3", AD, "<ActivityDiagram name='nome do diagrama'>\n<ActivityDiagramElements name='nome do bloco de elementos'>\n<StartNode id=3 name='nome do bloco inicial'/>\n<ActivityNode id=4 name='nome da atividade'/>\n<DecisionNode id=5 name='nome do nó de decisão'/>\n<MergeNode id=6 name='nome do nó de fusão'/>\n<FinalNode id=7 name='nome do nó final'/>\n</ActivityDiagramElements>\n<ActivityDiagramTransitions name='nome do nó de transições'>\n<Transition id=9/>\n<Transition id=10/>\n<Transition id=11/>\n<Transition id=12/>\n</ActivityDiagramTransitions>\n</ActivityDiagram>"]])
    def test_get_child_xml(self, name, node, expected):
        self.assertEqual(node.get_child_xml(), expected)
    @parameterized.expand([
        ["teste 4", [DN, SN], [AN], Exception],
        ["teste 5", [AN], [MN, MN], Exception],
        ["teste 6", [SN], [AN, SN], Exception],
        ["teste 7", [AN], [FN, FN], Exception],
    ])
    def test_Transition(self, name, source, target, expected):
        self.assertRaises(expected, Transition, source, target)
        
    @parameterized.expand([
        ["teste 8", ADE, [SN, SN], Exception]
    ])
    def test_AddChildren(self, name, element, children, expected):
        self.assertRaises(expected, element.add_children, children)
    @parameterized.expand([
        ["teste 9", ADE, SN, Exception]
    ])
    def test_AddChild(self, name, element, child, expected):
        self.assertRaises(expected, element.add_child, child)
        
    @parameterized.expand([
        ["teste 10", LS, "<Lifelines >\n<Lifeline id=15 name='nome da lifeline' />\n<Lifeline id=15 name='nome da lifeline' />\n<Lifeline id=15 name='nome da lifeline' />\n</Lifelines>"],
        ["teste 11", FS, "<Fragments>\n<Optional id=17 name='nome do fragmento' representedBy='nome do diagrama de sequencia'/>\n<Optional id=17 name='nome do fragmento' representedBy='nome do diagrama de sequencia'/>\n<Optional id=17 name='nome do fragmento' representedBy='nome do diagrama de sequencia'/>\n</Fragments>"],
        ["teste 12", SD, "<SequenceDiagram name='nome do diagrama'>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n<Fragment id=20 name='nome da mensagem' prob='valor da probabilidade'/>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n</SequenceDiagram>"],
        ["teste 13", SDS, "<SequenceDiagrams>\n<Lifelines >\n<Lifeline id=15 name='nome da lifeline' />\n<Lifeline id=15 name='nome da lifeline' />\n<Lifeline id=15 name='nome da lifeline' />\n</Lifelines>\n<Fragments>\n<Optional id=17 name='nome do fragmento' representedBy='nome do diagrama de sequencia'/>\n<Optional id=17 name='nome do fragmento' representedBy='nome do diagrama de sequencia'/>\n<Optional id=17 name='nome do fragmento' representedBy='nome do diagrama de sequencia'/>\n</Fragments>\n<SequenceDiagram name='nome do diagrama'>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n<Fragment id=20 name='nome da mensagem' prob='valor da probabilidade'/>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n</SequenceDiagram>\n<SequenceDiagram name='nome do diagrama'>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n<Fragment id=20 name='nome da mensagem' prob='valor da probabilidade'/>\n<Message id=19 name='nome da mensagem' prob='valor da probabilidade' source='nome da lifeline' target='nome da lifeline'/>\n</SequenceDiagram>\n</SequenceDiagrams>"]
    ])
    def test_get_child_xml1(self, name, node, expected):
        self.assertEqual(node.get_child_xml(), expected)