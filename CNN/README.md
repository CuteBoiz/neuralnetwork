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

[2. Neural Network]

</li>
<li>

[3. Convolutional Neural Network(CNN)](https://github.com/CuteBoiz/)
</li>
</ul>

</li>
<li> 

[II. CẤU TRÚC MẠNG CNN](https://github.com/CuteBoiz/)

</li>
<li>

[III. CÁCH LẬP TRÌNH TẠO RA CNN](https://github.com/CuteBoiz/)

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

## IMG 1

<p>Các function sử dụng trong một neuron thường được gọi là một Activation Funtion. Hiện nay có rất nhiều các Activation Function như: step, sigmoid, tanh, ReLU, leaky ReLU, …</p>

### 1. Activation Function

#### a. Step Function

<p> Một <i>Step Function</i> được định nghĩa bởi: </p>

## IMG 2

<p> Output sẽ bằng 1 nếu giá trị của x lớn hơn hoặc bằng không và bằng 0 nếu  x bé hơn không. Có thể thấy <i>Step Function</i>> có giá trị không đổi tại 0. </p>

<p> Hiện tại, các Neural Network sử dụng phương thức <i> Backpropagation</i> cùng với <i>Gradient Descent</i> để tính các <i>weights</i> cho các layer khác nhau. Vì <i>Step Function</i> có điểm không đổi tại 0 nên không còn phù hợp để dự đoán với <i> Gradient Descent</i> và không thể cập nhật các <i>weights</i>. </p>

<p>Để khắc phục điều này, <i>Sigmoid Function</i> đã được giới thiệu để khắc phục điểu này của <i>Step Function</i>.</p>

#### b. Sigmoid Function

<p>Một <i>Sigmoid Function</i> hay <i>Logistic Funtion</i> được định nghĩa:</p>

## IMG 3

<p>Giá trị của function hướng về 0 khi z hoặc biến độc lập hướng về âm vô cực, hướng về 1 khi z hướng về dương vô cực. Function này biểu diễn sự hội tụ sự hoạt động của các biến độc lập.</p>

<p>Vậy chúng ta dùng sigmoid function khi nào?</p>

<ul>
	<li>Sử dụng cho tập dữ liệu <b><i>không</i></b> tuyến tính.</li>
	<li><i>Sigmoid Function</i> khác nhau tại mọi điểm và do đó có thể sử dụng với GD và Backpropagation.</li>
</ul>

<p>Tuy nhiên, <i>Sigmoid Function</i> cũng gặp phải vấn đề về <i>“Vanishing Gradient”</i>. Có thể thấy từ hình trên rằng <i>Sigmoid Funciton</i> nén input của nó thành một phần rất nhỏ [0, 1] và có đạo hàm rất dốc. Vì vậy, những mảng input lớn còn sót lại, nơi nà đến những thay đổi lớn chỉ đưa ra những thay đổi rất nhỏ tại output.</p>

#### c. Tanh Function

<p>Tanh(z) Function là phiên bản cải tiến của sigmoid fucntion và output của nó nằm trong khoảng [-1, 1] thay vì [0, 1]</p>

## IMG4

<p>Lý do thông thường để dùng <i>Tanh Function</i> ở một số trường hợp thay cho <i>Sigmoid function</i> là vì khi dữ liệu nằm vòng quanh điểm 0, đạo hàm cao hơn. Và với độ dốc cao hơn sẽ giúp cải thiện <i>learning rate</i>.</p>

<p>Tuy nhiên Vanishing gradients vẫn tồn tại tại Tanh function. </p>

#### d. ReLU Function

<p><i>Rectified Linear Unit</i> được sử dụng rất nhiều trong các mô hình <i>Deep Learning</i>. Function này trả về 0 nếu nó nhận bất cứ giá trị input âm nào. Nhưng đối với các input dương nó sẽ trả về chính giá trị dương đó. Vì thế có thể viết f(x) = max(0, x).</p>

## IMG 5

### 2. Neural Network

<p>Chúng ta đã được biết qua về <i>Neuron</i> và <i>Activation Fucntion</i>. Bây giờ chũng ta sẽ đi sâu hơn về <i>Neural Network</i> và các biến thể của nó. </p>

<p>Trước khi hiểu về <i>Neural Network</i>, chúng ta cần biết được <i>Layer</i> bên trong chúng là gì. Một <i>Layer</i> không có nghĩa gì nhưng là một tập hợp các <i>Neuron</i> dùng để lấy các Input và đưa ra Output. Input của mỗi neuron được xử lí thông qua <i>Activation Function </i> định sẵn của mỗi neuron đó.</p>

## IMG 6

<p><i>Layer</i> bên trái ngoài cùng được gọi là <i>Input Layer</i>, và <i>Layer</i> bên phải ngoài cùng là <i>Output layer</i>. Các layer ở giữa được gọi là các <i>Hidden Layer</i> bởi vì giá trị của chúng không quan sát được bên trong. </p>

<p>Cũng có thể nói ví dụ trên bao gồm 3 Input Units <i>(không tính node bias)</i>, 3 Hidden Unit và 1 Output Unit.</p>

<p>Mỗi <i>Neural Network</i> đều phải có 1 Input và 1 Output Layer và một hoặc vài Hidden Layer.</p>

<p><b><i>Chú ý:</i></b> mỗi Hidden Layer có thể có <i>Activation Fuction</i> khác nhau. <b><i>Vd:</i></b> Hidden Layer 1 có thể dùng <i>Sigmoid Fuction</i>, Hidden Layer 2 có thể dùng <i>ReLU</i> và <i>Tanh Fucntion</i> tại lớp thứ 3. Chúng ta sẽ chọn <i>Activation Function</i> sao cho phù hợp với từng trường hợp dựa trên các loại dữ liệu được đưa ra.</p>

<p>Neural Network cần phải đưa ra dự đoán chính xác. Với mỗi Neuron ở mỗi layer đều có một giá trị <i>weight</i>. Đó chính là giá trị cần được cải thiện qua mỗi lần học từ dữ liệu của Neural Network. Và giải thuật học đó được gọi là <i>Backpropagration</i>.</p>

### 3. Covolutional Neural  Network (CNN)

<p>CNN là một biến thể của NN được sử dụng rộng rãi trong lĩnh vực <i>Computer Vision</i>. Tên gọi của CNN được đặt theo loại của Hidden Layer nằm bên trong nó.</p>

<p>Các Hidden Layer của CNN thông thường bao gồm <i>Convolution Layers</i>, <i>Pooling Layers</i>, <i>Fully Connected Layers</i> và <i>Normalzition Layers</i>.</p>

<p>Thay vì sử dụng các <i>Activation Function</i> ở bên trên thì CNN sử dụng là <i>Convolution Function</i> và <i>Pooling Fucntion</i>.</p>

## IMG 7

<p><b> a. Convolution Function:</b> Convolution hoạt động dựa trên 2 tín hiệu (ở 1D) hoặc 2 tín hiệu (ở 2D): một </i>input signal</p> là 1 bức ảnh và <i>signal</i> còn lại  là 1 <i>Filter</i> hay <i>Kernel</i>. Và từ các input sẽ tạo ra 1 ảnh Ouput được gọi là <i>Feature Map</i>.</p>

## IMG 8

<p><b> b. Pooling Function:</b> Pooling là quá trình phân tách lấy mẫu. Đối tượng được thay đổi cách biểu diễn (image, hidden layer output, matrix, …) giảm số chiều và cho phép để giả định  để tạo ra các feature chứa trong các sub-regions đã được giảm chiều.</p>

<p>Có 2 loại Pooling chính: <b><i>Max</i></b> và <b><i>Min pooling</i></b>.</p>

## IMG 9

<p>Vì vậy có thể xem CNN đơn giản là Deep Neural Network chứa các Hidden Layer bao gồm Covolution và Pooling Function. </p>

## II. CẤU TRÚC MẠNG CONVOLUTION NETWORK