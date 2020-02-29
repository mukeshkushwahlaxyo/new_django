@extends('layouts.master')
@section('content')
<main class="app-content">
	<div class="row">
        <div class="col-md-12 col-xl-12">
            <div class="card shadow-xs">
                <div class="col-md-12 col-xl-12" style="margin-top: 15px">
                    <h1 style="font-size: 24px">Leave Allotments</h1>
                </div>
                <div class="card-body table-responsive">
                    @if($message = Session::get('success'))
                        <div class="alert alert-success alert-block">
                            <button type="button" class="close" data-dismiss="alert">×</button>
                            {{$message}}
                        </div>
                    @endif
                    <table class="table table-striped table-hover" id="LeavesTable">
                        <thead>
                            <tr class="text-center">
                                <th>#</th>
                                <th>Name</th>
                                <th>Starts</th>
                                <th>Ends</th>
                                <th>Leaves</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            @php $count = 0;
                            @endphp
                            @if(count($allotments) != null)
                            @foreach($allotments as $index)
                                <tr class="text-center">
                                    <td>{{++$count}}</td>
                                    <td>{{ucwords($index->emp_name)}}</td>
                                    <td>{{$index['allotments'][0]->start}}</td>
                                    <td>{{$index['allotments'][0]->end}}</td>

                                    <td>
                                    @foreach($index->allotments as $leave)
                                        <div>{{ucwords($leave['leaves']->name)}} <span style="float: right">{{$leave->initial_bal}}</span></div>
                                        <hr>
                                    @endforeach
                                    </td>
                                    <td class='d-flex ' style="border-bottom:none">
                                  <span class="ml-2 text-center">
                                    <a href="{{route('allotments.edit', $index->user_id)}}" class="btn btn-sm btn-success">EDIT</i></a>
                                  </span>
                                    <span class="ml-2">
                                    @if(!empty($index['allotments'][0]->status) ? $index['allotments'][0]->status:'' == 1)
                                        <a href="{{route('hold.leave', $index->user_id)}}" class="btn btn-sm btn-info" onclick="return confirm('Are you sure?')">HOLD</a>
                                    @else
                                        <a href="{{route('reallot.leave', $index->user_id)}}" class="btn btn-sm btn-info" onclick="return confirm('Are you sure?')">Re-Allot</a>
                                    @endif
                                    </span>
                                <span class="ml-2">
                                    <form  action="{{route('allotments.destroy',$index->user_id)}}" method="POST" id="delform_{{ $index->user_id}}">
                                    @csrf
                                    @method('DELETE')
                                    <a href="javascript:$('#delform_{{ $index->user_id}}').submit();" class="btn btn-sm btn-danger" onclick="return confirm('Are you sure?')">DELETE</a>
                                    </form>
                                </span>
                                    </td>
                                </tr>
                            @endforeach
                            @endif
                        </tbody>
                    </table>
                </div> 
            </div>
        </div>
    </div>
</main>
<script type="text/javascript">
$(document).ready(function(){
    $('#LeavesTable').dataTable( {
    "ordering":   true,
    order   : [[1, 'asc']],
    "columnDefs": [ 
    { "orderable": false, "targets": 0,  }
    ]
  });


});
</script>
@endsection