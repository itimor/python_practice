import fetch from '@/utils/fetch';
import API from '@/config'

export function getblogList(query) {
  return fetch({
    url: API.getbloglist,
    method: 'get',
    params: query
  });
}

