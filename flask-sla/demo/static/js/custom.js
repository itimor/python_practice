$(document).ready(function() {
    "use strict";
    //初始化系统
    $('.leftpanel .nav-parent > a').live('click', function() {

      var parent = $(this).parent();
      var sub = parent.find('> ul');
      //console.log('hahahahah');
      // Dropdown works only when leftpanel is not collapsed
      if(!$('body').hasClass('leftpanel-collapsed')) {
         if(sub.is(':visible')) {
            sub.slideUp(200, function(){
               parent.removeClass('nav-active');
               $('.mainpanel').css({height: ''});
               adjustmainpanelheight();
            });
         } else {
            closeVisibleSubMenu();
            parent.addClass('nav-active');
            sub.slideDown(200, function(){
               adjustmainpanelheight();
            });
         }
      }
      return false;
   });

   function closeVisibleSubMenu() {
      $('.leftpanel .nav-parent').each(function() {
         var t = $(this);
         if(t.hasClass('nav-active')) {
            t.find('> ul').slideUp(200, function(){
               t.removeClass('nav-active');
            });
         }
      });
   }


   function adjustmainpanelheight() {
      // Adjust mainpanel height
      var docHeight = $(document).height();
      if(docHeight > $('.mainpanel').height())
         $('.mainpanel').height(docHeight);
   }
   adjustmainpanelheight();

   // Minimize Button in Panels
   $('.minimize').click(function(){
      var t = $(this);
      var p = t.closest('.panel');
      if(!$(this).hasClass('maximize')) {
         p.find('.panel-body, .panel-footer').slideUp(200);
         t.addClass('maximize');
         t.html('&plus;');
      } else {
         p.find('.panel-body, .panel-footer').slideDown(200);
         t.removeClass('maximize');
         t.html('&minus;');
      }
      return false;
   });


   // Add class everytime a mouse pointer hover over it
   $('.nav-bracket > li').hover(function(){
      $(this).addClass('nav-hover');
   }, function(){
      $(this).removeClass('nav-hover');
   });


   // Menu Toggle
   //$('.menutoggle').click(function(){
   $('.menutoggle').click(function(){
      var body = $('body');
      var bodypos = body.css('position');

      if(bodypos != 'relative') {

        if(!body.hasClass('leftpanel-collapsed')) {
            body.addClass('leftpanel-collapsed');
            $('.nav-bracket ul').attr('style','');
            $(this).addClass('menu-collapsed');

        }else{
            body.removeClass('leftpanel-collapsed chat-view');
            $('.nav-bracket li.active ul').css({display: 'block'});

            $(this).removeClass('menu-collapsed');

        }
        }else{

         if(body.hasClass('leftpanel-show'))
            body.removeClass('leftpanel-show');
         else
            body.addClass('leftpanel-show');

         adjustmainpanelheight();
      }

   });

   reposition_topnav();
   

   $(window).resize(function(){

      if($('body').css('position') == 'relative') {

         $('body').removeClass('leftpanel-collapsed chat-view');

      } else {

         $('body').removeClass('chat-relative-view');
         $('body').css({left: '', marginRight: ''});
    }

    reposition_topnav();

   });

   /* This function allows top navigation menu to move to left navigation menu
    * when viewed in screens lower than 1024px and will move it back when viewed
    * higher than 1024px
    */
   function reposition_topnav() {
      if($('.nav-horizontal').length > 0) {

         // top navigation move to left nav
         // .nav-horizontal will set position to relative when viewed in screen below 1024
         if($('.nav-horizontal').css('position') == 'relative') {

            if($('.leftpanel .nav-bracket').length == 2) {
               $('.nav-horizontal').insertAfter('.nav-bracket:eq(1)');
            } else {
               // only add to bottom if .nav-horizontal is not yet in the left panel
               if($('.leftpanel .nav-horizontal').length == 0)
                  $('.nav-horizontal').appendTo('.leftpanelinner');
            }

            $('.nav-horizontal').css({display: 'block'}).addClass('nav-pills nav-stacked nav-bracket');

            $('.nav-horizontal .children').removeClass('dropdown-menu');
            $('.nav-horizontal > li').each(function() {

               $(this).removeClass('open');
               $(this).find('a').removeAttr('class');
               $(this).find('a').removeAttr('data-toggle');

            });

            if($('.nav-horizontal li:last-child').has('form')) {
               $('.nav-horizontal li:last-child form').addClass('searchform').appendTo('.topnav');
               $('.nav-horizontal li:last-child').hide();
            }

         } else {
            // move nav only when .nav-horizontal is currently from leftpanel
            // that is viewed from screen size above 1024
            if($('.leftpanel .nav-horizontal').length > 0) {

               $('.nav-horizontal').removeClass('nav-pills nav-stacked nav-bracket').appendTo('.topnav');
               $('.nav-horizontal .children').addClass('dropdown-menu').removeAttr('style');
               $('.nav-horizontal li:last-child').show();
               $('.searchform').removeClass('searchform').appendTo('.nav-horizontal li:last-child .dropdown-menu');
               $('.nav-horizontal > li > a').each(function() {

                  $(this).parent().removeClass('nav-active');

                  if($(this).parent().find('.dropdown-menu').length > 0) {
                     $(this).attr('class','dropdown-toggle');
                     $(this).attr('data-toggle','dropdown');
                  }

               });
            }

         }

      }
   }


   // Sticky Header
   if($.cookie('sticky-header'))
      $('body').addClass('stickyheader');

   // Sticky Left Panel
   if($.cookie('sticky-leftpanel')) {
      $('body').addClass('stickyheader');
      $('.leftpanel').addClass('sticky-leftpanel');
   }

   // Left Panel Collapsed
   if($.cookie('leftpanel-collapsed')) {
      $('body').addClass('leftpanel-collapsed');
      $('.menutoggle').addClass('menu-collapsed');
   }

   


   // Check if leftpanel is collapsed
   if($('body').hasClass('leftpanel-collapsed'))
      $('.nav-bracket .children').css({display: ''});

   //图片管理
   $('.thmb').hover(function(){
      var t = $(this);
      t.find('.ckbox').show();
      t.find('.fm-group').show();
    }, function() {
      var t = $(this);
      if(!t.closest('.thmb').hasClass('checked')) {
        t.find('.ckbox').hide();
        t.find('.fm-group').hide();
      }
    });
    
    $('.ckbox').each(function(){
      var t = $(this);
      var parent = t.parent();
      if(t.find('input').is(':checked')) {
        t.show();
        parent.find('.fm-group').show();
        parent.addClass('checked');
      }
    });
    
    
    $('.ckbox').click(function(){
      var t = $(this);
      if(!t.find('input').is(':checked')) {
        t.closest('.thmb').removeClass('checked');
        enable_itemopt(false);
      } else {
        t.closest('.thmb').addClass('checked');
        enable_itemopt(true);
      }
    });
    
    $('#selectall').click(function(){
      if($(this).is(':checked')) {
        $('.thmb').each(function(){
          $(this).find('input').attr('checked',true);
          $(this).addClass('checked');
          $(this).find('.ckbox, .fm-group').show();
        });
        enable_itemopt(true);
      } else {
        $('.thmb').each(function(){
          $(this).find('input').attr('checked',false);
          $(this).removeClass('checked');
          $(this).find('.ckbox, .fm-group').hide();
        });
        enable_itemopt(false);
      }
    });
    
    function enable_itemopt(enable) {
      if(enable) {

        $('.itemopt').removeClass('disabled');
      } else {
        
        // check all thumbs if no remaining checks
        // before we can disabled the options
        var ch = false;
        $('.thmb').each(function(){
          if($(this).hasClass('checked'))
            ch = true;
        });
        
        if(!ch){
          $('.itemopt').each(function(){
             if(this.id !== 'uploadImg'){
                $(this).addClass('disabled');
             }
          })  
        }
      }
    }
    
    $("a[data-rel^='prettyPhoto']").prettyPhoto();


    //读取系统信息

    
    //获取请求参数
    var getUrlParams = function(filed){
        var results = new RegExp('[\?&]' + filed + '=([^&#]*)').exec(window.location.href);
        if (results==null){
            return null;
        }else{
            return results[1] || 0;
        }
    }

    
    $.fn.select2.defaults.set("theme", "bootstrap");
    //联系人选择框
    $("#choseBourse").select2({
        placeholder: '选择文交所',
        allowClear: true,
        name:"bourse",
    });

    $("#idfont").select2({
        placeholder: '选择正面照',
        allowClear: true,
        name:"idfont"
    });

    $("#idback").select2({
        placeholder: '选择反面照',
        allowClear: true,
        name:"idback"
    });

    //提交申请表格输入验证
    /*$('#ask-form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            bourse: {
                validators: {
                    callback: {
                        message: '请选择文交所',
                        callback: function(value, validator) {
                            var options = validator.getFieldElements('bourse').val();
                            return (options !== null && options !== "---");
                        }
                    }
                }
            },


            category:{
                validators: {
                    callback: {
                        message: '请选择品种',
                        callback: function(value, validator) {
                            var options = validator.getFieldElements('category').val();
                            return (options !== null && options !== "---");
                        }
                    }
                }
            },
            contact:{
               validators: {
                    callback: {
                        message: '请选择联系人',
                        callback: function(value, validator) {
                            var options = validator.getFieldElements('contact').val();
                            //var items = $('#captchaOperation').html().split(' '),
                            //    sum   = parseInt(items[0]) + parseInt(items[2]);
                            return (options != null && options != "---");
                        }
                    },
                }
            },
        }
    }).on('success.form.bv', function(e) {
            e.preventDefault();
            var $form = $(e.target);
            var bv = $form.data('bootstrapValidator');

            $.post($form.attr('action'), $form.serialize())
                .success( function(obj) {
                    bootbox.alert({
                        message:obj.msg,
                        callback:function(){
                            if(obj.success){
                                location.href=obj.url;
                            }
                        }
                    })
                })
                .fail( function(xhr, status, error) {
                    console.log(error);
                })
    });  
       
    $("#ask-cancle").click(function(){
        $('#ask-form').data('bootstrapValidator').resetForm();
        //location.href = "/index.php?m=user&a=showHome";
    }); */


    //联系人表格
    function detailFormatter(index, row) {
            //console.log(row);
            //var html = [];
            var html = '<div class="row">'+
                '<div class="col-md-6">'+
                '<a href="'+row.frontgraph+'"  target="_blank" class="thumbnail">'+
                '<img src="'+row.frontgraph +'"'+'alt="附件"></a>'+
                '</div>'+
                '<div class="col-md-6">'+
                '<a href="'+row.backgraph+'"  target="_blank" class="thumbnail">'+
                '<img src="'+row.backgraph +'"'+'alt="附件"></a>'+
                '</div>'+
                '</div>';
            return html;
        }    


    $('#user-contact-tb').bootstrapTable({
        url: '/index.php?a=getContactList&c=user',
        smartDisplay:true,
        idField :'id',
        cache:true,
        showColumns:true,
        showHeader:true,
        showRefresh:true,
        showExport:true,
        pagination:true,
        sidePagination:'client',
        search:true,
        dataField:'data',
        showToggle:true,
        detailView:true,
        clickToSelect:true,
        checkboxHeader:true,
        detailFormatter:detailFormatter,
        contentType:'application/json',
        columns: [
        {
            field: 'realname',
            title: '姓名',
            sortable:true,
        },{
            field: 'idcardno',
            title: '证件号码',
            searchable:true
        },{
            field: 'frontgraph',
            title: '正面照',
            visible:false,
            editable:{
                mode:'inline',
                placeholder:'请选择正面照',
                type:'select2',
                inputclass:'sel-xs',
                tpl: '<select style="width:150px;">',
                url:'/index.php?c=user&a=updateContact',
                success:function(resp,newvlue){
                    if(resp.success){
                        bootbox.alert({
                            message: resp.msg,
                            size:'large',
                            callback:function(){
                                $('#user-contact-tb').bootstrapTable('refresh');
                            }
                        });
                    }
                },
                display:function(value,source){
                  if( source == undefined){
                    $(this).text(value.split('/').pop());    
                  }
                },
                select2: {
                    placeholder: '选择照片',
                    allowClear: true,
                    ajax: {
                        url: '/index.php?c=user&a=getImageList',
                        dataType: 'json',
                        processResults: function (obj) {
                            return {
                                results: $.map(obj.data, function (item) {
                                    return {
                                        text: item.img_desc,
                                        id: item.img_path
                                    }
                                })
                            };
                        }
                    }
                }  
            },
            
        },{
            field: 'backgraph',
            title: '反面照',
            visible:false,
            editable:{
              mode:'inline',
              placeholder:'请选择反面照',
              type:'select2',
              tpl: '<select style="width:150px;">',
              inputclass:'sel-xs',
              url:'/index.php?c=user&a=updateContact',
              success:function(resp,newvlue){
                if(resp.success){
                  bootbox.alert({
                    message: resp.msg,
                    size:'large',
                    callback:function(){
                      $('#user-contact-tb').bootstrapTable('refresh');
                    }
                  });
                  }
              },
              display:function(value,source){
                if( source == undefined){
                  $(this).text(value.split('/').pop());
                }
              },
              select2: {
                placeholder: '选择照片',
                allowClear: true,
                ajax: {
                  url: '/index.php?c=user&a=getImageList',
                  dataType: 'json',
                  processResults: function (obj) {
                    return {
                      results: $.map(obj.data, function (item) {
                        return {
                          text: item.img_desc,
                          id: item.img_path
                        }
                      })
                    };
                  }
                }
              }  
            },
            
        },{
            field: 'cellphone',
            title: '手机/电话',
            searchable:true
        },{
            field: 'bourse',
            title: '文交所'
        },{
            field: 'account',
            title: '账号'
        },{
            field: '__',
            align:'center',
            title: '操作',
            formatter: function (v, r, idx) {
        
              var id = 'del-'+r.id;
              return '<button class="btn btn-primary" id='+id+' value='+r.realname+'>删除</button>'  
                       
            }

        }]
    }).on('post-body.bs.table',function(){
        $("button[id^=del-]").click(function(){
            var cid = this.id.replace(/[^0-9]/ig,"");
            var name =$(this).eq(0).val();
            bootbox.confirm('请问要删除联系人<span class="label label-danger">'+name+'</span>吗?', function (result) {
                if(result){
                    $.ajax({
                        type:'POST',
                        url:'/index.php?a=delContact&c=user',
                        data:{id:cid},
                        success:function(obj){
                            bootbox.alert({
                                message:obj.msg,
                                callback:function(){
                                    if(obj.success){
                                        $('#user-contact-tb').bootstrapTable('refresh');
                                    }
                                }
                            }); 
                        },
                        dataType:'json'
                    });
                }
            }); 
        });
        
    });

    //联系人输入验证
    $('#contactform').bootstrapValidator({
        message: '输入值不合法',
        excluded: [':disabled'],
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            name: {
                message: '输入的联系人姓名不合法',
                validators: {
                    notEmpty: {
                        message: '联系人姓名不能为空',
                    },
                    regexp: {
                        regexp: /[\u4E00-\u9FA5\uF900-\uFA2D]/,
                        message: '请输入正确的中文名字',
                    },
                }
            },
            cardno: {
                message: '请输入正确的身份证号码',
                validators: {
                    notEmpty: {
                        message: '身份证号码不能为空',
                    },
                    regexp: {
                        regexp: /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/,
                        message: '请输入正确的15或18位身份证号码',
                    },

                }
            },
            bourse:{
                validators: {
                    callback: {
                        message: '请选择文交所',
                        callback: function(value, validator) {
                            var options = validator.getFieldElements('bourse').val();
                            return (options !== null && options !== "---");
                        }
                    }
                }
            },
            phone: {
                validators: {
                    notEmpty: {
                        message: '手机号码不能为空'
                    },
                    regexp: {
                        regexp: /^1[3|4|5|8|7][0-9]\d{8}$/,
                        message: '输入的手机号不正确',
                    },
                }
            },
            zhanghao:{
               validators: {
                    notEmpty: {
                        message: '文交所账号不能为空'
                    },
                }
            },
            idfont:{
                validators: {
                    callback: {
                        message: '请选择身份证正面照片',
                        callback: function(value, validator) {
                            var options = validator.getFieldElements('idfont').val();
                            return (options !== null && options !== "---");
                        }
                    }
                }
            },
            idback:{
                validators: {
                    callback: {
                        message: '请选择身份证反面照片',
                        callback: function(value, validator) {
                            var options = validator.getFieldElements('idback').val();
                            return (options !== null && options !== "---");
                        }
                    }
                }
            },
             
        }
    }).on('success.form.bv', function(e) {
            e.preventDefault();
            var $form = $(e.target);
            var bv = $form.data('bootstrapValidator');
            //console.log($form.serialize());

            $.post($form.attr('action'), $form.serialize())
                .success( function(obj) {
                    //alert(msg.info);
                    bootbox.alert({
                        message:obj.msg,
                        callback:function(){
                            if(obj.success){
                                location.reload();
                            }
                        }
                    });
                 })
                .fail( function(xhr, status, error) {
                    console.log(error);
                    //console.log(msg)
                })
        });



    $("#btn_rest").click(function(){
         $('#contactform').data('bootstrapValidator').resetForm();
    });


    //用户列表
    $('#users-table').bootstrapTable({
        url:'/admin.php?c=User&a=getUserList',
        //smartDisplay:true,
        cache:false,
        dataField:'data',
        showHeader:true,
        showRefresh:true,
        showExport:true,
        showColumns:true,
        pagination:true,
        sidePagination:'client',
        showToggle:true,
        search:true,
        contentType:'application/json',
        columns: [
            {
                field: 'name',
                title: '用户名',
                searchable:true
            },{
                field: 'create_time',
                title: '注册日期',
                sortable:true,
            },{
                field: 'isOk',
                title: '是否启用',
                formatter:function(v,r,idx){
                    if(v == 1){
                        return  '<span class="label label-success">已启用</span>';
                    }else{
                        return  '<span class="label label-danger">已禁用</span>'
                    }
                }
            },{
                field: '__',
                align:'center',
                title: '操作',
                formatter: function (v, r, idx) {
                     return '<button class="btn btn-default" type="button">禁用</button><button class="btn btn-default" type="button">重置密码</button>'
                }
        }]
    });

    
    
    //用户订单管理
    
    

    //上传照片
    $('#uploadImg').click(function(){
        bootbox.dialog({
            title: "上传照片",
            size:'large',
            message: '<div class="row">  ' +
                '<div class="col-md-12"> ' +
                '<div class="alert alert-warning" id="image-alert" style="display:none">'+
                '<a href="#" class="close" onclick="$(this).parent().hide()">'+
                '    &times;'+
                ' </a>'+
                '<strong>警告！</strong>图片名称,上传文件不能为空!'+
                ' </div>'+
                '</div>'+
                '<div class="col-md-12"> ' +
                '<form class="form-horizontal" id="imgForm"> ' +
                '<div class="form-group"> ' +
                '<label class="col-md-2 control-label" for="name">图片名称</label> ' +
                '<div class="col-md-8"> ' +
                '<input type="text" class="form-control" name="img_desc"> ' +
                '<div class="help-block">例如:xxx正面照</div>'+
                '</div> ' +
                '</div> ' +
                '<div class="form-group"> ' +
                '<label class="col-md-2 control-label" for="name">选择文件</label> ' +
                '<div class="col-md-8"> ' +
                '<input type="file" class="file-upload" id="upload-image"> ' +
                '</div> ' +
                '</div> ' +
                '</form> </div>  </div>',
                buttons: {
                    success: {
                        label: "上传",
                        className: "btn-success",
                        callback: function (e) {
                          var desc  = $('input[name^="img_desc"]').val();
                          var path = $('input[name^="path"]').val();
                          if(desc && path){
                            $.ajax({
                              type:'POST',
                              url:'/index.php?a=addImage&c=user',
                              data:{desc:desc,path:path},
                              success:function(obj){
                                  bootbox.alert({
                                      message:obj.msg,
                                      callback:function(){
                                          if(obj.success){
                                              //location.href = obj.url;
                                              location.reload();
                                          }
                                      }
                                  });
                              },
                              dataType:'json'
                            });
                          }else{
                            $('#image-alert').show();
                            return false;
                          }
                        }
                    }
                }
        }).bind('shown.bs.modal',function(){
            var  fileup = $('#upload-image');
            fileup.fileinput({
                language: 'zh',
                uploadUrl: '/index.php?a=uploadImage&c=user',
                uploadAsync:false,
                showUpload:false,
                showCaption:false,
                showRemove:false,
                showUploadedThumbs:false,
                allowedFileExtensions : ['jpg', 'png'],
                minFileCount:1,
                maxFileCount:5,
                maxFileSize:500,
                browseClass: "btn btn-primary",
                previewFileIcon: "<i class='glyphicon glyphicon-king'></i>",
            }).on('filebatchselected',function(event,files){
              $(this).fileinput("upload");
            }).on('filebatchuploadsuccess',function(event, data, previewId, index){
              $("#imgForm").append('<input type="hidden" name="path" value="'+data.response.path+'" />');
            }).on('filesuccessremove',function(event,id){
              if(id){
                $("input[name='path']").prop('disabled', true);
              }
            });
        })
    });


    function closeVisibleSubMenu() {
        $('.leftpanel .nav-parent').each(function() {
            var t = $(this);
            if(t.hasClass('nav-active')) {
                t.find('> ul').slideUp(200, function(){
                    t.removeClass('nav-active');
                });
            }
        });
    }

    function adjustmainpanelheight() {
        // Adjust mainpanel height
        var docHeight = $(document).height();
        if(docHeight > $('.mainpanel').height())
            $('.mainpanel').height(docHeight+300);
    }
    adjustmainpanelheight();


    // Tooltip
    $('.tooltips').tooltip({ container: 'body'});

    // Popover
    $('.popovers').popover();

    // Close Button in Panels
    $('.panel .panel-close').click(function(){
        $(this).closest('.panel').fadeOut(200);
        return false;
    });
   
    //form-wizard
    var $validator = $("#firstForm").validate({
        highlight: function(element) {
          $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        success: function(element) {
          $(element).closest('.form-group').removeClass('has-error');
        },
        rules:{
            bourse:"required",
            category:"required",
            contact:"required",
            //luckyno:"required",

        },
        messages:{
            bourse:"请选择文交所",
            category:"请选择产品",
            contact:"请选择联系人",
            luckyno:'请填入中签号'
        }
      });
      
      $('#validationWizard').bootstrapWizard({
        tabClass: 'nav nav-pills nav-justified nav-disabled-click',
        onTabClick: function(tab, navigation, index) {
          return false;
        },
        onNext: function(tab, navigation, index) {
            var $valid = $('#firstForm').valid();
            if(!$valid) {
                $validator.focusInvalid();
                return false;
            }
            var $total = navigation.find('li').length;
            var $current = index+1;
            if($current == $total) {
                $("#vtab"+$current).html('asdasdada!!!');
            }
          
          
        }
    });

  
    $('#logout').click(function(){
        $.ajax({
            type:'POST',
            url:'index.php?a=doLogout',
            success:function(obj){
                if(obj.success){
                    //location.href = "/index.php?a=login";
                    location.href = obj.url;
                }else{
                    bootbox.alert({
                        message:obj.msg
                    })
                }
            },
            dataType:'json'
        });
    });
});


