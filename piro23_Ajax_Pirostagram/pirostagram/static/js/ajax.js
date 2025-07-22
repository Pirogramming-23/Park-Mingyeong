// 좋아요 토글
$(document).on('click', '.like-btn', function() {
    var btn = $(this);
    var postId = btn.data('post-id');
    $.ajax({
        url: btn.data('like-url'),
        type: "POST",
        data: {
            'post_id': postId,
            'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        success: function(response) {
            btn.find('.like-count').text(response.like_count);
            if (response.liked) {
                btn.css('color', 'red');
            } else {
                btn.css('color', 'black');
            }
        },
        error: function(xhr) {
            alert('좋아요 실패: ' + (xhr.responseJSON?.error || xhr.status));
        }
    });
});

// 댓글 작성
$(document).on('submit', '.comment-form', function(e) {
    e.preventDefault();
    var form = $(this);
    var postId = form.data('post-id');
    var content = form.find('input[name="content"]').val();
    $.ajax({
        url: form.data('add-url'),
        type: "POST",
        data: {
            'post_id': postId,
            'content': content,
            'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        success: function(response) {
            if (response.id) {
                var commentHtml = '<div data-comment-id="' + response.id + '"><b>' + response.author + '</b>: ' + response.content +
                    ' <button class="comment-delete-btn" data-comment-id="' + response.id + '">삭제</button></div>';
                form.prev('.comment-list').append(commentHtml);
                form.find('input[name="content"]').val('');
            }
        },
        error: function(xhr) {
            alert('댓글 작성 실패: ' + (xhr.responseJSON?.error || xhr.status));
        }
    });
});

// 댓글 삭제
$(document).on('click', '.comment-delete-btn', function() {
    var btn = $(this);
    var commentId = btn.data('comment-id');
    $.ajax({
        url: window.COMMENT_DELETE_URL,
        type: "POST",
        data: {
            'comment_id': commentId,
            'csrfmiddlewaretoken': window.CSRF_TOKEN
        },
        success: function(response) {
            if (response.success) {
                btn.parent().remove();
            } else {
                alert(response.error || "삭제 실패");
            }
        },
        error: function(xhr) {
            alert('댓글 삭제 실패: ' + (xhr.responseJSON?.error || xhr.status));
        }
    });
}); 