import IECore

import Gaffer

import AtomsGaffer

import DocumentationAlgo

Gaffer.Metadata.registerNode(

    AtomsGaffer.AtomsCrowdGenerator,

    "description",
    """
    Generates a fully deformed crowd of agents by combining the input crowd points
    from the primary scene, and the specified agents from the right-hand scene.
    """,

    "icon", "atoms_logo.png",
    "documentation:url", DocumentationAlgo.documentationURL,

    plugs = {

        "parent" : [

            "description",
            """
			The location of the crowd points in the input scene. The
			per-vertex primitive variable "\agentType\" will be used
			to determine which agents to instantiate. It must contain
			indexed string data (ie. as generated by AtomsCrowdReader).
			"""

        ],

        "name" : [

            "description",
            """
            The name of the new location containing the generated agents.
            """,

        ],

        "agents" : [

            "description",
            """
			The scene containing the agents to be applied to each vertex of
			the crowd. Specify multiple agents by parenting them at the root
			of the scene :

			- /agent0
			- /agent1
			- /agent2

			Be sure to order the agents to match the \"agentType\" data provided
			on the input crowd points.

			Note that the agents are not limited to being a
			single object : they can each have arbitrary child
			hierarchies.
			""",

            "plugValueWidget:type", "",

        ],

        "attributes" : [

            "description",
            """
			The names of per-vertex primitive variables to be turned into
			per-agent attributes. Names should be separated by spaces and
			can use Gaffer's standard wildcards.
			""",

        ],

    },

)
