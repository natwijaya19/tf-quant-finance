<!--
This file is generated by a tool. Do not edit directly.
For open-source contributions the docs will be updated automatically.
-->

*Last updated: 2021-10-27.*

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf_quant_finance.math.qmc.utils.log2" />
<meta itemprop="path" content="Stable" />
</div>

# tf_quant_finance.math.qmc.utils.log2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/google/tf-quant-finance/blob/master/tf_quant_finance/math/qmc/utils.py">View source</a>



Returns the point-wise base-2 logarithm a given `Tensor`.

```python
tf_quant_finance.math.qmc.utils.log2(
    value
)
```



<!-- Placeholder for "Used in" -->

```python
import tensorflow as tf
import tf_quant_finance as tff

# Example: Computing the base-2 logarithm of a given vector.

tff.math.qmc.utils.log2(tf.constant([1, 2, 4, 8, 16], dtype=tf.float32))
# ==> tf.Tensor([0., 1., 2., 3., 4.], shape=(5,), dtype=float32)
```

#### Args:


* <b>`value`</b>: Positive scalar `Tensor` of real values.


#### Returns:

`Tensor` with the same `shape` and `dtype` as `value` equal to `ln(value) /
ln(2)`.