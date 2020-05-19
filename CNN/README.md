# Convolution Neural Network

## Table of Contents

<ul>
<li> 

[I. NEURAL NETWORK LÀ GÌ](https://github.com/CuteBoiz/) 

</li>
<li> 

[II. CẤU TRÚC MẠNG CNN](https://github.com/CuteBoiz/)

</li>
<li>

[III. CÁCH LẬP TRÌNH TẠO RA CNN](https://github.com/CuteBoiz/)

</li>
</ul>

## I. NEURAL NETWORK LÀ GÌ ?

<p>Neural Network là một trong những thuật toán machine learning phổ biến nhất hiện tại. Điều đó đã được chứng minh bởi Neural Networks vượt qua các giải thuật khác về hiệu quả cũng như tốc độ. Với một số biến thể như CNN, RNN, Autoencoders, DeepLearning, …</p>

<p>Neural Network dần được các nhà nghiên cứu dữ liệu hoặc các người tìm hiểu về machine learning Vì vậy chúng ta cần có một cái nhìn tổng quan về Neural Network là gì, chúng cấu thành từ những thứ gì, ưu điểm và khuyết điểm của chúng.</p>

#### Neuron là gì?

<p>Cái tên đã cho thấy, cụm từ <i>Neural Network</i> được lấy cảm hứng bởi hệ thống cấu trúc neural tại bộ não của con người, và cũng như bộ não người các khối cấu tạo nên chúng được gọi là <i>Neuron</i>. Chức năng của chúng cũng tương tự như các neuron của con người: Chúng nhận vào nhiều input và đưa ra một output.</p>

<p>Đối với lĩnh vực toán học, một Neuron trong thế giới Machine Learning là một placeholder cho một phép toán, và công việc duy nhất của chúng là đưa ra một output bằng cách áp dụng phép toán trên các input cho sẵn.</p>

##IMG 1

<p>Các function sử dụng trong một neuron thường được gọi là một Activation Funtion. Hiện nay có rất nhiều các Activation Function như: step, sigmoid, tanh, ReLU, leaky ReLU, …</p>

### 1. Activation Function

#### a. Step Function

<p> Một <i>Step Function</i> được định nghĩa bởi: </p>

##IMG 2

<p> Output sẽ bằng 1 nếu giá trị của x lớn hơn hoặc bằng không và bằng 0 nếu  x bé hơn không. Có thể thấy <i>Step Function</i>> có giá trị không đổi tại 0. </p>

<p> Hiện tại, các Neural Network sử dụng phương thức <i> Back Propagation</i> cùng với <i>Gradient Descent</i> để tính các <i>weights</i> cho các layer khác nhau. Vì <i>Step Function</i> có điểm không đổi tại 0 nên không còn phù hợp để dự đoán với <i> Gradient Descent</i> và không thể cập nhật các <i>weights</i>. </p>

<p>Để khắc phục điều này, <i>Sigmoid Function</i> đã được giới thiệu để khắc phục điểu này của <i>Step Function</i>.</p>

#### b. Sigmoid Function