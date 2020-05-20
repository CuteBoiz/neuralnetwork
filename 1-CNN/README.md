# Convolution Neural Network

## Table of Contents

<ul>
<li> 

[I. NEURAL NETWORK LÀ GÌ](https://github.com/CuteBoiz/) 

<ul>
<li>

[Neuron là gì?](https://github.com/CuteBoiz/)

</li>
<li>

[1. Activation Function](https://github.com/CuteBoiz/)

</li>
<li>

[2. Neural Network](https://github.com/CuteBoiz/)

</li>
<li>

[3. Convolutional Neural Network(CNN)](https://github.com/CuteBoiz/)
</li>
</ul>

</li>
<li> 

[II. CẤU TRÚC MẠNG CNN](https://github.com/CuteBoiz/)

<ul>
<li>

[1. Local Receptive Field](https://github.com/CuteBoiz/)

</li>
<li>

[2. Shared Weight and Biases](https://github.com/CuteBoiz/)

</li>
<li>

[3. Pooling Layers](https://github.com/CuteBoiz/)

</li>
</ul>
</li>
<li>

[III. CÁCH LẬP TRÌNH TẠO RA CNN](https://github.com/CuteBoiz/)

<ul>
<li>

[1. Đọc Ảnh Đầu Vào](https://github.com/CuteBoiz/)

</li>
<li>

[2. Chuẩn Bị Kernel](https://github.com/CuteBoiz/)

</li>
<li>

[3. Convolution Layers](https://github.com/CuteBoiz/)

</li>
<li>

[4. ReLU Layers](https://github.com/CuteBoiz/)

</li>
<li>

[5. Max Pooling Layers](https://github.com/CuteBoiz/)

</li>
</ul>
</li>
<li>

[IV. NGUỒN THAM KHẢO](https://github.com/CuteBoiz/)
</li>
</ul>

## I. NEURAL NETWORK LÀ GÌ ?

<p>Neural Network là một trong những thuật toán machine learning phổ biến nhất hiện tại. Điều đó đã được chứng minh bởi Neural Networks vượt qua các giải thuật khác về hiệu quả cũng như tốc độ. Với một số biến thể như CNN, RNN, Autoencoders, DeepLearning, …</p>

<p>Neural Network dần được các nhà nghiên cứu dữ liệu hoặc các người tìm hiểu về machine learning Vì vậy chúng ta cần có một cái nhìn tổng quan về Neural Network là gì, chúng cấu thành từ những thứ gì, ưu điểm và khuyết điểm của chúng.</p>

#### Neuron là gì?

<p>Cái tên đã cho thấy, cụm từ <i>Neural Network</i> được lấy cảm hứng bởi hệ thống cấu trúc neural tại bộ não của con người, và cũng như bộ não người các khối cấu tạo nên chúng được gọi là <i>Neuron</i>. Chức năng của chúng cũng tương tự như các neuron của con người: Chúng nhận vào nhiều input và đưa ra một output.</p>

<p>Đối với lĩnh vực toán học, một Neuron trong thế giới Machine Learning là một placeholder cho một phép toán, và công việc duy nhất của chúng là đưa ra một output bằng cách áp dụng phép toán trên các input cho sẵn.</p>

<a href="https://imgur.com/Jlt4tqS"><img src="https://i.imgur.com/Jlt4tqS.png" title="source: imgur.com" height="200" width="450" /></a>

<p>Các function sử dụng trong một neuron thường được gọi là một Activation Funtion. Hiện nay có rất nhiều các Activation Function như: step, sigmoid, tanh, ReLU, leaky ReLU, …</p>

### 1. Activation Function

#### a. Step Function

<p> Một <i>Step Function</i> được định nghĩa bởi: </p>

<a href="https://imgur.com/k7Ex6sG"><img src="https://i.imgur.com/k7Ex6sG.png" title="source: imgur.com" /></a>

<p> Output sẽ bằng 1 nếu giá trị của x lớn hơn hoặc bằng không và bằng 0 nếu  x bé hơn không. Có thể thấy <i>Step Function</i>> có giá trị không đổi tại 0. </p>

<p> Hiện tại, các Neural Network sử dụng phương thức <i> Backpropagation</i> cùng với <i>Gradient Descent</i> để tính các <i>weights</i> cho các layer khác nhau. Vì <i>Step Function</i> có điểm không đổi tại 0 nên không còn phù hợp để dự đoán với <i> Gradient Descent</i> và không thể cập nhật các <i>weights</i>. </p>

<p>Để khắc phục điều này, <i>Sigmoid Function</i> đã được giới thiệu để khắc phục điểu này của <i>Step Function</i>.</p>

#### b. Sigmoid Function

<p>Một <i>Sigmoid Function</i> hay <i>Logistic Funtion</i> được định nghĩa:</p>

<a href="https://imgur.com/A61qqsq"><img src="https://i.imgur.com/A61qqsq.png" title="source: imgur.com" /></a>

<p>Giá trị của function hướng về 0 khi z hoặc biến độc lập hướng về âm vô cực, hướng về 1 khi z hướng về dương vô cực. Function này biểu diễn sự hội tụ sự hoạt động của các biến độc lập.</p>

<p>Vậy chúng ta dùng sigmoid function khi nào?</p>

<ul>
	<li>Sử dụng cho tập dữ liệu <b><i>không</i></b> tuyến tính.</li>
	<li><i>Sigmoid Function</i> khác nhau tại mọi điểm và do đó có thể sử dụng với GD và Backpropagation.</li>
</ul>

<p>Tuy nhiên, <i>Sigmoid Function</i> cũng gặp phải vấn đề về <i>“Vanishing Gradient”</i>. Có thể thấy từ hình trên rằng <i>Sigmoid Funciton</i> nén input của nó thành một phần rất nhỏ [0, 1] và có đạo hàm rất dốc. Vì vậy, những mảng input lớn còn sót lại, nơi nà đến những thay đổi lớn chỉ đưa ra những thay đổi rất nhỏ tại output.</p>

#### c. Tanh Function

<p>Tanh(z) Function là phiên bản cải tiến của sigmoid fucntion và output của nó nằm trong khoảng [-1, 1] thay vì [0, 1]</p>

<a href="https://imgur.com/WkmFDTc"><img src="https://i.imgur.com/WkmFDTc.png" title="source: imgur.com" /></a>

<p>Lý do thông thường để dùng <i>Tanh Function</i> ở một số trường hợp thay cho <i>Sigmoid function</i> là vì khi dữ liệu nằm vòng quanh điểm 0, đạo hàm cao hơn. Và với độ dốc cao hơn sẽ giúp cải thiện <i>learning rate</i>.</p>

<p>Tuy nhiên Vanishing gradients vẫn tồn tại tại Tanh function. </p>

#### d. ReLU Function

<p><i>Rectified Linear Unit</i> được sử dụng rất nhiều trong các mô hình <i>Deep Learning</i>. Function này trả về 0 nếu nó nhận bất cứ giá trị input âm nào. Nhưng đối với các input dương nó sẽ trả về chính giá trị dương đó. Vì thế có thể viết f(x) = max(0, x).</p>

<a href="https://imgur.com/aZ7d2XK"><img src="https://i.imgur.com/aZ7d2XK.png" title="source: imgur.com" /></a>

### 2. Neural Network

<p>Chúng ta đã được biết qua về <i>Neuron</i> và <i>Activation Fucntion</i>. Bây giờ chũng ta sẽ đi sâu hơn về <i>Neural Network</i> và các biến thể của nó. </p>

<p>Trước khi hiểu về <i>Neural Network</i>, chúng ta cần biết được <i>Layer</i> bên trong chúng là gì. Một <i>Layer</i> không có nghĩa gì nhưng là một tập hợp các <i>Neuron</i> dùng để lấy các Input và đưa ra Output. Input của mỗi neuron được xử lí thông qua <i>Activation Function </i> định sẵn của mỗi neuron đó.</p>

<a href="https://imgur.com/nLmWrgr"><img src="https://i.imgur.com/nLmWrgr.png" title="source: imgur.com" /></a>

<p><i>Layer</i> bên trái ngoài cùng được gọi là <i>Input Layer</i>, và <i>Layer</i> bên phải ngoài cùng là <i>Output layer</i>. Các layer ở giữa được gọi là các <i>Hidden Layer</i> bởi vì giá trị của chúng không quan sát được bên trong. </p>

<p>Cũng có thể nói ví dụ trên bao gồm 3 Input Units <i>(không tính node bias)</i>, 3 Hidden Unit và 1 Output Unit.</p>

<p>Mỗi <i>Neural Network</i> đều phải có 1 Input và 1 Output Layer và một hoặc vài Hidden Layer.</p>

<p><b><i>Chú ý:</i></b> mỗi Hidden Layer có thể có <i>Activation Fuction</i> khác nhau. <b><i>Vd:</i></b> Hidden Layer 1 có thể dùng <i>Sigmoid Fuction</i>, Hidden Layer 2 có thể dùng <i>ReLU</i> và <i>Tanh Fucntion</i> tại lớp thứ 3. Chúng ta sẽ chọn <i>Activation Function</i> sao cho phù hợp với từng trường hợp dựa trên các loại dữ liệu được đưa ra.</p>

<p>Neural Network cần phải đưa ra dự đoán chính xác. Với mỗi Neuron ở mỗi layer đều có một giá trị <i>weight</i>. Đó chính là giá trị cần được cải thiện qua mỗi lần học từ dữ liệu của Neural Network. Và giải thuật học đó được gọi là <i>Backpropagration</i>.</p>

### 3. Covolutional Neural  Network (CNN)

<p>CNN là một biến thể của NN được sử dụng rộng rãi trong lĩnh vực <i>Computer Vision</i>. Tên gọi của CNN được đặt theo loại của Hidden Layer nằm bên trong nó.</p>

<p>Các Hidden Layer của CNN thông thường bao gồm <i>Convolution Layers</i>, <i>Pooling Layers</i>, <i>Fully Connected Layers</i> và <i>Normalzition Layers</i>.</p>

<p>Thay vì sử dụng các <i>Activation Function</i> ở bên trên thì CNN sử dụng là <i>Convolution Function</i> và <i>Pooling Fucntion</i>.</p>

<a href="https://imgur.com/fwYw8XC"><img src="https://i.imgur.com/fwYw8XC.png" title="source: imgur.com" /></a>

<p><b> a. Convolution Function:</b> Convolution hoạt động dựa trên 2 tín hiệu (ở 1D) hoặc 2 tín hiệu (ở 2D): một </i>input signal</p> là 1 bức ảnh và <i>signal</i> còn lại  là 1 <i>Filter</i> hay <i>Kernel</i>. Và từ các input sẽ tạo ra 1 ảnh Ouput được gọi là <i>Feature Map</i>.</p>

<a href="https://imgur.com/QlqXMrq"><img src="https://i.imgur.com/QlqXMrq.png" title="source: imgur.com" /></a>

<p><b> b. Pooling Function:</b> Pooling là quá trình phân tách lấy mẫu. Đối tượng được thay đổi cách biểu diễn (image, hidden layer output, matrix, …) giảm số chiều và cho phép để giả định  để tạo ra các feature chứa trong các sub-regions đã được giảm chiều.</p>

<p>Có 2 loại Pooling chính: <b><i>Max</i></b> và <b><i>Min pooling</i></b>.</p>

<a href="https://imgur.com/spyNBvx"><img src="https://i.imgur.com/spyNBvx.png" title="source: imgur.com" /></a>

<p>Vì vậy có thể xem CNN đơn giản là Deep Neural Network chứa các Hidden Layer bao gồm Covolution và Pooling Function. </p>

## II. CẤU TRÚC MẠNG CONVOLUTION NETWORK

<p>Mạng CNN sử dụng 3 ý tưởng cơ bản:</p>

<ul>
	<li>Local Receptive Field</li>
	<li>Shared weights and biases</li>
	<li>Pooling</li>
</ul>

### 1. Local Receptive Field (Trường tiếp nhận cục bộ)

<p>Đầu vào của mạng CNN là một ảnh. <b><i>Vd:</i></b> ảnh có kích thước 28x28 và giá trị mỗi điểm ảnh là một ô trong ma trận. Trong mô hình NN truyền thống thì chúng ta sẽ kết nối các neuron thành 1 chuỗi với nhau.</p>

<p>Tuy nhiên đối với CNN, chỉ cần kết nối trong vùng nhỏ của các đầu neuron đầu vào với các filter. Ta có thể tạo ra 1 hidden layer bằng cách sau:</p>

<p>Tạo ra neuron ẩn đầu tiên trong lớp ẩn 1</p>

<a href="https://imgur.com/3LYrv9C"><img src="https://i.imgur.com/3LYrv9C.png" title="source: imgur.com" /></a>

<p>Dịch filter qua bên phải 1 cột sẽ tạo được neuron ẩn thứ 2</p>

<a href="https://imgur.com/BqlnoIX"><img src="https://i.imgur.com/BqlnoIX.png" title="source: imgur.com" /></a>

<p>Với ảnh 28x28 và filter 5x5 ta sẽ tạo được ma trận ẩn (28 - 5 + 1)  = 24x24</p>

<p>Như vậy, local receptive field thích hợp cho việc phân tách dữ liệu ảnh, giúp chọn ra những vùng ảnh có giá trị nhất cho việc đánh giá phân lớp. </p>

### 2. Shared Weights and Biases (Trọng số chia sẻ)

<p>Trọng số chia sẻ giúp chúng ta có thể phát hiện được 1 feature ở các vị trí khác nhau trên ảnh. </p>

<p>Cho filter như hình bên dưới:</p>

<a href="https://imgur.com/ycsjjYv"><img src="https://i.imgur.com/ycsjjYv.png" title="source: imgur.com" /></a>

<p></p>

<a href="https://imgur.com/C9gLz6n"><img src="https://i.imgur.com/C9gLz6n.png" title="source: imgur.com" /></a>

<p>Apply filter vào ảnh trong trường tiếp nhận cục bộ: </p>

<a href="https://imgur.com/qILEz6L"><img src="https://i.imgur.com/qILEz6L.png" title="source: imgur.com" /></a>

<p>Cơ bản, bên trong ảnh đầu vào nếu có một feature tương tự với filter sẽ cho ra một kết quả lớn. Nếu chuyến filter sang khu vực khác không trùng với filter thì sẽ cho kết quả bằng 0:</p>

<p>Vì thế, convolution sẽ tìm ra được đúng đường cong trong filter dù nó nằm ở bất cứ đâu trên ảnh. </p>

<p>Với cấu trúc trên ta sẽ có thể phát hiện được chỉ một feature. Vì vậy nếu dùng nó cho các bài toán lớn hơn như phát hiện khuôn mặt thì ta sẽ cần nhiều hơn một feature map. Và 1 convolutional layer hoàn chỉnh sẽ bao gồm nhiều feature maps.</p>

<a href="https://imgur.com/A2JeChm"><img src="https://i.imgur.com/A2JeChm.png" title="source: imgur.com" /></a>

<p>Điểm mạnh lớn nhất của sharing weights and biases là giảm mạnh số các thông số bên trong convolutional network.</p>

<p>Với mỗi feature map ta cần 25 (5 x 5) shared wieght, cộng thêm 1 shared bias. Vì vậy mỗi feature map sẽ có 26 thông số. Nếu có 20 feature map thì ta sẽ có 20x26 = 520 thông số cho 1 CNN bé hơn rất nhiều so với NN thông thường với lớp đầu tiên 28x28 = 784 với 30 hidden neuron thì sẽ có 784x30 +30 = 23550 thông số.</p>

### 3. Pooling Layers

<p>Ngoài các lớp trên, CNN còn có các Pooling Layers. Pooling Layer thường được dùng ngay sau các Convolutional Layer. Chức năng của lớp này là đơn giản hóa giảm bớt số lượng neuron đầu ra của Convolutional Layer.</p>

<a href="https://imgur.com/V8RNGvP"><img src="https://i.imgur.com/V8RNGvP.png" title="source: imgur.com" /></a>

<p>Nếu áp dùng Pooling cho map 24x24 thì sau khi pooling Feature map đó sẽ chỉ còn lại kích thước 12x12</p>

<a href="https://imgur.com/ffdXrCb"><img src="https://i.imgur.com/ffdXrCb.png" title="source: imgur.com" /></a>

<p>Ta có thể cho rằng max-pooling như một cách tìm feature được phát hiện ở vùng nào trên ảnh. Sau đó nó sẽ đưa ra thông tin vị trí chính xác. Một lợi ích lớn là có ít hơn nhiều các pooled feature vì vậy chúng giúp giảm số lượng lớn các thông số cho các lớp sau này.</p>

## III. CÁCH LẬP TRÌNH CONVOLUTIONAL NEURAL NETWORK

<p><b>Các bước để tạo ra CNN</b></p>

<ul>
	<li>Đọc input image</li>
	<li>Chuẩn bị Kernel(Filter)</li>
	<li><b><i>Convolution Layer:</i></b> tích chập từng kernel với input image tạo ra các Feature Map</li>
	<li><b><i>ReLU Layer:</i></b> Áp dụng ReLU Activation funciton vào feature map</li>
	<li><b><i>Max Pooling Layer:</i></b> Sử dụng max pooling vào output của ReLU Layer</li>
</ul>

### Bước 1: Đọc Ảnh Đầu Vào

<p>Ta sẽ dùng thư viện skimage Python và chuyển ảnh RGB về Gray</p>

```python
import skimage.data
import numpy as np
import cv2
import sys

img = skimage.data.chelsea()

img = skimage.color.rgb2gray(img)
```

<p>Ảnh đầu vào: </p>

<a href="https://imgur.com/wswHAyt"><img src="https://i.imgur.com/wswHAyt.png" title="source: imgur.com" /></a>

### Bước 2: Chuẩn Bị Kernel

<p>Convulution hay tích chập là nhân từng phần tử trong ma trận 3. Sliding windows hay còn gọi là kernel, filter hoặc feature detect là một ma trận vuông có kich thước nhỏ 3x3 hoặc 5x5</p>

```python
l1_filter = np.zeros((2, 3, 3))
l1_filter[0, :, :] = np.array([[[-1, 0, 1],
				[-1, 0, 1],
				[-1, 0, 1]]])

l1_filter[1, :, :] = np.array([[[1, 1, 1],
				[0, 0, 0],
				[-1, -1, -1]]])
```

### Bước 3: 

<p>Covolution là nhân từng phần tử của ma trận kernel với ảnh đầu vào. Kết quả nhận được một ma trận được gọi là <b><i>Feature Maps</i></b> hay <b><i>Convolved Feature</i></b>.</p>

<a href="https://imgur.com/WDBRG2x"><img src="https://i.imgur.com/WDBRG2x.png" title="source: imgur.com" /></a>

```python
feature_maps = conv(img, l1_filter)
```

```python
def conv(img, conv_filter):
	if len(img.shape) > 2 or len(conv_filter.shape) > 3:
		if img.shape[-1] != conv_filter.shape[-1]:
			print("Error: Number of channels of image and filter must match")
			sys.exit()
	if conv_filter.shape[1] != conv_filter.shape[2]: # Check if filter dimensions are equal.  
		print('Error: Filter must be a square matrix. I.e. number of rows and columns must match.')
		sys.exit()
	if conv_filter.shape[1] % 2 == 0:
		print('Error: Filter must have an odd size. I.e. number of rows and columns must be odd.')
		sys.exit()

	feature_maps = np.zeros((img.shape[0] - conv_filter.shape[1] + 1,
							img.shape[1] - conv_filter.shape[2] + 1,
							conv_filter.shape[0]))

	for filter_num in range(conv_filter.shape[0]):
		print("Filter", filter_num + 1)
		curr_filter = conv_filter[filter_num]
		print(curr_filter)
		feature_maps[:, :, filter_num] = conv_(img, curr_filter)
	return feature_maps
```



<p>Function bắt đầu từ việc kiểm tra điều kiện của img và filter để có thể tiến hành covolution:</p>

<ul>
	<li>Nếu là ảnh màu thì depth của ảnh và filter phải bằng nhau</li>
	<li>Filter phải là ma trận vuông và có số chiều là lẻ (3x3, 5x5, 7x7, …)</li>
</ul>

```python
if len(img.shape) > 2 or len(conv_filter.shape) > 3:
	if img.shape[-1] != conv_filter.shape[-1]:
		print("Error: Number of channels of image and filter must match")
		sys.exit()
	if conv_filter.shape[1] != conv_filter.shape[2]: # Check if filter dimensions are equal.  
		print('Error: Filter must be a square matrix. I.e. number of rows and columns must match.')
		sys.exit()
	if conv_filter.shape[1] % 2 == 0:
		print('Error: Filter must have an odd size. I.e. number of rows and columns must be odd.')
		sys.exit()
```


<p>Tiếp đến sẽ tạo ra một ma trận rỗng để chứa feature image:</p>

<ul>
	<li>Dimesion của feature image khi không có stride và padding  
	[image.x – filter.x + 1, image.y – filter.y + 1, số filter]</li>
</ul>

```python
feature_maps = np.zeros((img.shape[0] - conv_filter.shape[1] + 1,
				img.shape[1] - conv_filter.shape[2] + 1,
				conv_filter.shape[0]))
```


<p>Sau đó sẽ convolution từng filter vào ảnh đầu vào và lưu vào feature image rỗng:</p>

```python
for filter_num in range(conv_filter.shape[0]):
	print("Filter", filter_num + 1)
	curr_filter = conv_filter[filter_num]
	print(curr_filter)
	feature_maps[:, :, filter_num] = conv_(img, curr_filter)
```


<p> Thuật Toán Convolution: </p>

```python
def conv_(img, filter): 
	filter_size = filter.shape[0]
	result = np.zeros((img.shape))
	x = np.uint16(filter_size/2)
	#Looping through the image to apply the convolution operation.
	for r in np.arange(0, img.shape[0]-x-2):
		for c in np.arange(0, img.shape[1]-x-2):
			curr_region = img[r:r+filter_size, c:c+filter_size]
			curr_result = curr_region * filter
			result[r, c] = np.sum(curr_result)

	final_result = result[x:result.shape[0]-x, x:result.shape[1]-x]
	return final_result
```

<a href="https://imgur.com/3p7Z89M"><img src="https://i.imgur.com/3p7Z89M.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/yPKr99C"><img src="https://i.imgur.com/yPKr99C.png" title="source: imgur.com" /></a>

<p>Từng output của mỗi filter sau đó sẽ được đưa vào ReLU Layer</p>

### Bước 4: ReLU Activation Function

```python
relu_maps = ReLU(feature_maps)

```

```python
def ReLU(feature_maps):
	relu_out = np.zeros((feature_maps.shape))
	for map_num in range (feature_maps.shape[-1]):
		for r in np.arange(0, feature_maps.shape[0]):
			for c in np.arange(0, feature_maps.shape[1]):
				relu_out[r, c, map_num] = np.max(feature_maps[r, c, map_num], 0)
	return relu_out
```

<p>Thuật toán relu là chỉ cần lặp qua từng phần tử của feature image nếu phần từ đó lớn hơn bằng 0 thì vẫn là chính nó, nếu nó bé hơn 0 thì sẽ bằng 0</p>

<a href="https://imgur.com/Q6pgEGk"><img src="https://i.imgur.com/Q6pgEGk.png" title="source: imgur.com" height="" width="" /></a>

<a href="https://imgur.com/kPzYrSp"><img src="https://i.imgur.com/kPzYrSp.png" title="source: imgur.com" /></a>

### Bước 5: Max Pooling Layer

```python
pool_map = pooling(relu_maps, 2, 2)

```

```python
def pooling(feature_maps, size=2, stride=2):
	pool_out = np.zeros((np.uint16((feature_maps.shape[0]-size+1)/stride),
						np.uint16((feature_maps.shape[1]-size+1)/stride),
						feature_maps.shape[-1]))
	for map_num in range(feature_maps.shape[-1]):
		r_out = 0
		for r in np.arange(0, feature_maps.shape[0]-size-1, stride):
			c_out = 0
			for c in np.arange(0, feature_maps.shape[1]-size-1, stride):
				pool_out[r_out, c_out, map_num] = np.max(feature_maps[r:r+size, c:c+size])
				c_out = c_out + 1
			r_out = r_out + 1
	return pool_out
```

<a href="https://imgur.com/KWosq0w"><img src="https://i.imgur.com/KWosq0w.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/NYGtO11"><img src="https://i.imgur.com/NYGtO11.png" title="source: imgur.com" /></a>


## IV. NGUỒN THAM KHẢO

<ul>
	<li><a href="https://www.kdnuggets.com/2018/04/building-convolutional-neural-network-numpy-scratch.html">https://www.kdnuggets.com/2018/04/building-convolutional-neural-network-numpy-scratch.html</li>
	<li><a href="https://towardsdatascience.com/covolutional-neural-network-cb0883dd6529">https://towardsdatascience.com/covolutional-neural-network-cb0883dd6529</li>
	<li><a href="https://chsasank.github.io/deep-learning-crash-course-2.html">https://chsasank.github.io/deep-learning-crash-course-2.html</li>
	<li><a href="https://towardsdatascience.com/understanding-neural-networks-from-neuron-to-rnn-cnn-and-deep-learning-cd88e90e0a90">https://towardsdatascience.com/understanding-neural-networks-from-neuron-to-rnn-cnn-and-deep-learning-cd88e90e0a90</li>
</ul>