using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace IWPandDatabase.Models
{
    public class Key
    {
        [Display(Name = "PublicKey"), Required]
        public string PublicKey { get; set; }

        [Display(Name = "PrivateKey"), Required]
        public string PrivateKey { get; set; }
    }
}