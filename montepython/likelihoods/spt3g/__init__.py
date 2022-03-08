# there is no specific likelihood code for this experiment, because it
# falls in the category of CMB experiments described in the "mock CMB"
# format. The class below inherits the properties of a general class
# "Likelihood_mock_cmb", which knows how to deal with all experiments in
# "mock CMB" format.

from montepython.likelihood_class import Likelihood_spt3g


class spt3g(Likelihood_spt3g):
    pass
