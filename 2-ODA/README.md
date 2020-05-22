## OBJECT DETECTION ALGORITHMS

## Table of Contents
<ul>
<li>

[I. INTRODUCTION](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[II. REGION-COVOLUTIONAL NEURAL NETWORK(R-CNN)](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[III. FAST REGION-COVOLUTIONAL NEURAL NETWORK](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[IV. FASTER REGION-COVOLUTIONAL NEURAL NETWORK](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[V. YOU ONLY LOOK ONCE (YOLO)](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
<li>

[VI. SOURCE](https://github.com/CuteBoiz/neuralnetwork/tree/master/)

</li>
</ul>


## I. INTRODUCTION

<p>Thị giác máy tính là một lĩnh vực liên ngành có sức hút rất lớn trong những năm gần đây(từ khi có CNN) và một lĩnh vực không thể thiếu của thị giác máy tính đó là <i>Object Detection</i>. <i>Object Detection</i> giúp ích rất nhiều trong giao thông, bảo mật, giám sát, … </p>

<p>Sự khác biệt giữa giải thuật Object Detection và giải thuật phân lớp là trong giải thuật Detection chúng ta sẽ vẽ các <b><i>Bounding Box</i></b> xung quanh các vật thể cần tìm bên trong ảnh. Như vậy, bạn cũng không nhất thiết vẽ chỉ 1 <i>Bounding Box</i>, có thể có nhiều <i>Bounding Box</i> tượng trưng cho những vật khác nhau trong cũng một ảnh.</p>

<a href="https://imgur.com/Ix8GLa4"><img src="https://i.imgur.com/Ix8GLa4.png" title="source: imgur.com" /></a>

## II. REGION-COVOLUTIONAL NEURAL NETWORK(R-CNN)

<p>Để tránh khỏi vấn đề về chọn số lượng lớn các phân vùng, nhóm của <i>Ross Girshick</i> đã dề xuất một phương pháp sử dụng <b><i>Selective Search</i></b> để trích ra 2000 vùng trong ảnh và gọi đó là các <b><i>Proposal Region</i></b> (Vùng trọng điểm). Vì thế thay vì nhận dạng số lượng lớn các phân vùng, thì với giải thuật này ta chỉ cần làm việc với 2000 vùng. Và 2000 vùng này có thể được tạo ra nhờ giải thuật <i>Selective Search</i>:  </p>

<ul>
	<li>Tạo ra số lượng lớn các phân vùng phụ khởi tạo</li>
	<li>Sử dụng giải thuật tham lam (Greedy Algorithm) để kết hợp đệ quy các vùng tương tự nhau thành các vùng lớn hơn</li>
	<li>Sử dụng những phân vùng đã được kết hợp đó để tạo ra các <b><i>Proposal Region</i></b></li>
</ul>

<a href="https://imgur.com/qy65KRI"><img src="https://i.imgur.com/qy65KRI.png" title="source: imgur.com" /></a>

<p>2000 vùng này sẽ được bao bọc trong các khung để đưa vào CNN và tạo ra<i> Feature Vector</i> có 4096-chiều. CNN có chức năng như một <b><i>Feature Extractor</i></b> và đầu ra sẽ chứa những <i>Feature</i> trích xuất được từ ảnh và được đưa vào các <b><i>SVM</i></b>(Support Vector Machine) để phân loại sự hiện diện của vật thể bên trong các <i>Proposal Regions</i>.</p>

<p>Thuật toán này có thể dự đoán sự hiện diện của con người nhưng khuôn mặt có thể bên trong vùng đó có thể bị cắt đôi. Vì thế, những offset value giúp điều chỉnh những <i>Bounding Box</i> của <i>Proposal Region</i> này.</p>

<a href="https://imgur.com/ggKrlAu"><img src="https://i.imgur.com/ggKrlAu.png" title="source: imgur.com" /></a>

<p>Điểm yếu của R-CNN</p>

<ul>
	<li>Vẫn tốn rất nhiều thời gian để train vì cần xác định 2000 vùng cho mỗi ảnh</li>
	<li>Không thể thực hiện reatime vì cần đến 47s cho mỗi ảnh test</li>
	<li>Selective search là một giải thuật cố định. Vì thế sẽ không thể training tại bước này. Điều này sẽ tạo ra những <i><b>Bad</b> Proposal Region</i>.</li>
</ul>


## III. FAST REGION-COVOLUTIONAL NEURAL NETWORK

<a href="https://imgur.com/CJTJceR"><img src="https://i.imgur.com/CJTJceR.png" title="source: imgur.com" /></a>

<p>Tác giả của <i><b>R-CNN</b></i> đã giải quyết những vấn đề của R-CNN bằng cách tạo ra một thuật toán nhanh hơn được gọi là <b><i>Fast R-CNN</i></b>. Cách tiếp cận tương tự với <i>R-CNN</i>, nhưng thay vì đưa các <i>Proposal Region</i> vào CNN thì ta đưa ảnh input vào trực tiếp CNN để tạo ra các <b><i>Feature map</i></b>. Và từ các <i>Feature Map</i> ta sẽ xác định các <i>Proposal Region</i> và bọc chúng trong các khung và sau đó sử dụng <b><i>RoI Pooling Layer</i></b> ta reshape chúng thành kích cỡ cố định để có thể đưa vào <i>Fully Connected Layer</i>. Từ <i>RoI Feature Vector</i>, chúng ta sẽ dụng <i>Softmax Layer</i> để dự đoán class cho các <i>Proposed Region</i> và các <i>Offset Value</i> cho <i>Bounding Box</i>.</p>

<p>Lý do <i>Fast R-CNN</i> nhanh hơn <i>R-CNN</i> là vì Fast R-CNN không cần phải đưa cả 2000 vùng trọng điểm vào CNN và <i>convolution</i> với mỗi vùng. Mà thay vào đó ta chỉ cần thực hiện <i>covolution</i> với ảnh đầu vào và với <i>Feature Map</i> được tạo ra bởi ảnh đó. </p>

<a href="https://imgur.com/5Jdo7LU"><img src="https://i.imgur.com/5Jdo7LU.png" title="source: imgur.com" /></a>

## IV. FASTER REGION-COVOLUTIONAL NEURAL NETWORK

<a href="https://imgur.com/nbbI57r"><img src="https://i.imgur.com/nbbI57r.png" title="source: imgur.com" height="500" width="550" /></a>

<p>Cả 2 thuật toán R-CNN và Fast R-CNN đêu sử dụng <i>Selective Search</i> để tìm ra các <i>Proposal Region. Selective Search</i> là một thuật toán chậm và tốn thời gian và ảnh hưởng không nhỏ đến hiệu suất của toàn bộ network. Vì thế nhóm của Shaoqing Ren đã đưa ra một giải thuật Object Detection loại bỏ <i>Selective Search</i> và để network học cách lấy các vùng trọng điểm.</p>

<p>Tương tự như Fast R-CNN, Faster R-CNN đưa ảnh input vào CNN để tạo ra các <i>Feature Map</i>. Và thay vì sử dụng <i>Selective Search</i> để tìm các vùng trọng điểm thì một network độc lập khác sẽ được sử dụng để dự đoán các vùng này. Những vùng được dự đoán này sẽ được đưa đến <i>RoI Pooling Layer</i> để reshape và sau đó sẽ được xác định class.</p>

<a href="https://imgur.com/hzkX3yT"><img src="https://i.imgur.com/hzkX3yT.png" title="source: imgur.com" height="300" width="500" /></a>

<p>Bảng trên cho thấy Faster R-CNN nhanh hơn rất nhiều so với các tiền nhiệm . Vì thế Faster R-CNN có thể được sử dụng cho việc nhận dạng vật thể thười gian thực (Real-time Object Detection).</p>

## V. YOU ONLY LOOK ONCE (YOLO)

<p>Những thuật toán bên trên đều sử dùng các <b><i>vùng</i></b> để xác định vị trí của các vật thể bên trong ảnh. Network sẽ không nhìn toàn bộ bức ảnh và được thay bằng từng phần của bức ảnh sẽ với khả năng cao chứa vật thể. YOLO hay You Only Look Once là một giải thuật phát hiện vật thể khác xa với các giải thuật trên. Trong YOLO một CNN dự đoán các bounding box và xác suất các lớp cho các box này.</p>

<a href="https://imgur.com/tvrsHS4"><img src="https://i.imgur.com/tvrsHS4.png" title="source: imgur.com" /></a>

<p>Cách YOLO hoạt động là lấy một  ảnh và chia ra thành lưới SxS. Bên trong mỗi ô ta lấy m Bounding Box. Cho mỗi Bounding Box , network đưa ra xác suất thuộc class và offset value cho bounding box đó. Những Bounding Box có xác suất vượt ngưỡng sẽ được chọn và sử dụng để định vị vật thể bên trong ảnh.</p>

<p>YOLO sở hữu tốc độ nhanh (45 fps) hơn các giải thuật phát hiện vật thể khác. Giới hạn của YOLO là phát hiện các vật thể nhỏ. vd: sẽ khá khó nếu tìm bầy chim trong ảnh. Điều này dẫn tới hạn chế về không gian của giải thuật.</p>

## VI. SOURCE

<ul>
<li>

[https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)

</li>
</ul>