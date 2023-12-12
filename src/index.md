# RBPBench

[RBPBench](https://usegalaxy.eu/root?tool_id=toolshed.g2.bx.psu.edu/repos/rnateam/rbpbench/rbpbench/0.7+galaxy0) is multi-function tool to evaluate CLIP-seq and other genomic region data
using a comprehensive collection of known RBP binding motifs. RBPBench can be used
for a variety of purposes, from RBP motif search (database or user-supplied RBPs)
in genomic regions, over motif co-occurrence analysis, to benchmarking CLIP-seq peak
caller methods as well as comparisons across cell types and CLIP-seq protocols.

## [RBPBench Webserver on Galaxy](https://usegalaxy.eu/root?tool_id=toolshed.g2.bx.psu.edu/repos/rnateam/rbpbench/rbpbench/0.7+galaxy0)

## RBPBench Galaxy Tutorials

- [Basic Galaxy introduction and RBPBench user interface](docs/tutorial/intro.md)

## RBPBench results

![RBPBench example visualizations](assets/images/rbpbench_visualization_examples.png)
<span style="font-size: 90%;">
**Figure**: Some example visualizations produced by RBPBench.
**a**: RBP binding motif co-occurrence heat map.
**b**: What RBP binding motif combinations appear in the data.
**c**: Motif distances in the data relative to an RBP of interest.
**d**: To which region types RBPs preferentially bind to.
**e**: Comparing CLIP-seq peak calling methods.
**f**: Comparing experimental conditions.
</span>

## Additional Links

RBPBench [GitHub repository](https://github.com/michauhl/RBPBench)

RBPBench [Bioconda package](https://bioconda.github.io/recipes/rbpbench/README.html)

## RBP motif data

List of [RBPs and number of available motifs per RBP](docs/tutorial/RBPs.md)
