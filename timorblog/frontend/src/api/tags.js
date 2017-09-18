import fetch from '@/utils/fetch';
import API from '@/config'

export function gettagList(query) {
  return fetch({
    url: API.gettaglist,
    method: 'get',
    params: query
  });
}
